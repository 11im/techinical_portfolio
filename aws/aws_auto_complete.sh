#!/bin/bash

# Linux & Mac

# AWS Completer Search
# which aws_completer

# Add Path : change if /usr/local/bin/  differs from  'which aws_completer'
export PATH=/usr/local/bin/:$PATH

# change ~/.profile with ~/.bash_profile  or ~/.bash_login
# if zsh, ~/.zshrc
source ~/.profile

# if zsh add following command in front of complete command
# autoload bashcompinit && bashcompinit
# autoload -Uz compinit && compinit
complete -C '/usr/local/bin/aws_completer' aws