#!/bin/bash

# Start a new detached session
tmux new-session -d

tmux select-pane -t 0

# Attach to the session
tmux attach
 