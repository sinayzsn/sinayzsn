#!/bin/bash

# Export Oh My Zsh themes and configurations
cd ~ && tar -czf ohmyzsh_themes.tar.gz .oh-my-zsh/custom/themes
cd ~ && tar -czf ohmyzsh_config.tar.gz .zshrc .p10k.zsh

# Export Powerlevel10k theme and configurations
cd ~ && tar -czf powerlevel10k_themes.tar.gz .p10k.zsh-theme
