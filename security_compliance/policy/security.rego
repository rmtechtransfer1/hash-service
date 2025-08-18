package main

# Check for privileged containers
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  container.securityContext.privileged == true
  msg := "Containers cannot run in privileged mode"
}

# Check readOnlyRootFilesystem - with proper null handling
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  # Check if readOnlyRootFilesystem is not explicitly set to true
  not container.securityContext.readOnlyRootFilesystem == true
  msg := sprintf("Container '%s' must have readOnlyRootFilesystem: true", [container.name])
}

# Allow local images with :latest for Kind
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  endswith(container.image, ":latest")
  # Only deny if it's from a registry (has a slash)
  contains(container.image, "/")
  contains(container.image, ".")  # Has domain
  msg := sprintf("Container '%s' uses :latest tag from registry - pin to specific version", [container.name])
}