#!/bin/bash

## Система
TARGET=/opt
TARGET_BIN=/usr/local/bin
## Домашний каталог
# TARGET=~/opt
# TARGET_BIN=~/.local/bin


## Получить тег
TAG=`basename $(curl -sL -o /dev/null -w %{url_effective} https://github.com/quarto-dev/quarto-cli/releases/latest)`
TAG=${TAG/v/}

## Скачать
cd /tmp
wget https://github.com/quarto-dev/quarto-cli/releases/download/v${TAG}/quarto-${TAG}-linux-amd64.tar.gz

## Распаковать
mkdir -p ${TARGET}
tar -C ${TARGET} -xvzf /tmp/quarto-${TAG}-linux-amd64.tar.gz
mv ${TARGET}/quarto-${TAG} ${TARGET}/quarto

## Симлинк на исполняемый файл
mkdir -p ${TARGET_BIN}
ln -s ${TARGET}/quarto/bin/quarto ${TARGET_BIN}/quarto