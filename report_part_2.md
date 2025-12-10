## Part 2 Report

I completed the Part 2 tasks working solo as a make-up assignment.

### Renaming changes
I renamed the `player` components to `Pacman` across all source files and test files to match the updated project specification.  
This included updating:
- class names  
- variable names  
- imports  
- references inside tests  

### Cleanup changes
I removed the accidentally committed `.env` file, added it to `.gitignore`, and rewrote the Git history to remove the sensitive file from all previous commits.

### Git workflow
I created a feature branch (`part2-renaming`) and opened a pull request into `main`.  
All changes were reviewed and merged following a standard Git workflow.

### Continuous Integration
I added a GitHub Actions CI workflow that:
- installs dependencies  
- runs `black` for code formatting  
- runs `flake8` for linting  
- runs `pytest` for automated tests  

The workflow is configured to run on pushes and pull requests to `main`.

### Summary
All required changes for Part 2 were completed successfully, and the repository is now clean, consistent, and passing automated checks.
