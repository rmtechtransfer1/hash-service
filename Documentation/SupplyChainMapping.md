# Supply Chain Mapping

## Compile & unit tests
- pytest (Python) / CMAKE/Ctest (C++)
- Security Concept: Reproducible Build
- SLSA: L3 (Hardened builds), supports provenance completeness/accuracy
- NIST 800-53 Controls: SA-11 (testing); SI-2 (flaw remediation), SA-15 (Development Process)
- DISA STIG/SRG: repeatable builds & tests (general SRG expectation)

## Static Analysis
- Bandit (Python) / Clang-tidy (C++)
- Security Concept: C++ SAST
- SLSA: hardened build hygiene toward Build L3
- NIST 800-53 Controls: SA-11 (static analysis)
- DISA STIG/SRG: flaw detection pre-release (App/Container SRG)

## Supply Chain Security
- CycloneDX
- Security Concept: SPDX Format Conversion
- SLSA Level: L2 (Provenance exists)
- NIST 800-53 Controls: SR-3 (supply-chain)
- DISA STIG: management and mitigation of risks associated with 3rd party software

## SLSA Generator
- Security Concept: Build Provenance
- SLSA: achieves Build L2/L3
- NIST 8800-53 Controls: SI-7 (integrity)
- DISA STIG/SRG: supports trusted build pipeline expectations

## Cosign
- Security Concept: Container Signing (Keyless)
- SLSA: Build L2/L3 authenticity when paired with builder-issued provenance
- NIST 800-53 Controls: SI-7 (integrity), SC-12/SC-13 (crypto management/protection)
- DISA STIG/SRG: verify signed images; FIPS-validated crypto

## Container Security
- Trivy (Vulnerability Scan)
- Security Concept: CVE Scanning
- SLSA: guardrails toward reproducible, policy-governed builds
- NIST 800-53 Controls: SA-15 (Automated Vulnerability Analysis)
- DISA STIG/SRG: verify system is free from vulnerabilities

## Trivy (Config Scan)
- Trivy (Configuration Scan)
- Security Concept: Misconfiguration Detection
- NIST 800-53 Controls: CM-6 (Configuration Settings), SA-15 (	Automated Vulnerability Analysis)
- DISA STIG/SRG:: verify system is free from misconfigurations

## Config/K8s policy scan
- Tools: Trivy (config), Conftest/OPA
- Security Concept: Policy as Code
- SLSA: guardrails toward reproducible, policy-governed builds
- NIST 800-53 Controls: CM-7 (Least Functionality), AC-3 (Access Enforcement)
- DISA STIG/SRG: K8s STIG—admission/policy controls (non-root, readOnlyRootFilesystem, etc.)