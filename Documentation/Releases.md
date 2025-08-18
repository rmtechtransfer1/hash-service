# 1. Update version in your files (if applicable)
Update version in CMakeLists.txt, package.json, etc.

# 2. Update CHANGELOG (if you maintain one)
echo "## v1.0.0 - $(date +%Y-%m-%d)" >> CHANGELOG.md
echo "- Feature: Added new functionality" >> CHANGELOG.md
echo "- Fix: Resolved issueb" >> CHANGELOG.md

# 3. Commit version updates
git add .
git commit -m "chore: prepare release v1.0.0"
git push origin main

# 4. Wait for CI to pass on main branch

# 5. Then create and push the tag
git tag -a v1.0.0 -m "Release v1.0.0: <brief description>"
git push origin v1.0.0