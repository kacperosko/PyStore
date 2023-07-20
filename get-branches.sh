#!/bin/bash

# Fetch all remote branches
git fetch

# Iterate over each remote branch
for branch in $(git branch -r | grep -v HEAD); do
    # Get the last commit date and relative time
    last_commit_date=$(git show --format="%cd" --date=format:"%Y-%m-%d" $branch | head -n 1)

    # Print the last commit date and branch name
    echo -e "$last_commit_date\t$branch"
done | LC_COLLATE=C sort -r

