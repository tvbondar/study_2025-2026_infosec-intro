#!/bin/bash

# release.sh — автоматизация релизов по Git Flow + Conventional Commits + GitHub

set -e

# Проверка аргументов
if [ $# -lt 2 ]; then
  echo "Использование: $0 <version> <release_notes>"
  exit 1
fi

VERSION=$1
RELEASE_NOTES=$2

echo "=== Создание релиза версии $VERSION ==="

# 1. Инициализация git flow, если не сделано
if ! git flow config > /dev/null 2>&1; then
  echo "Инициализация git flow..."
  git flow init -d
fi

# 2. Проверка незавершённых релизов
EXISTING_RELEASE=$(git branch | grep 'release/')
if [ ! -z "$EXISTING_RELEASE" ]; then
  echo "Найдена незавершённая релизная ветка: $EXISTING_RELEASE"
  echo "Сначала завершите её или выполните: git flow release abort <release>"
  exit 1
fi

# 3. Переключаемся на develop
git checkout develop

# 4. Добавляем все новые файлы
git add .
git commit -m "chore: подготовка к релизу $VERSION" || echo "Нет новых изменений для коммита"

# 5. Создаём релизную ветку
git flow release start $VERSION

# 6. Генерируем CHANGELOG через standard-version
if ! command -v standard-version >/dev/null 2>&1; then
  echo "Установите standard-version: pnpm add -g standard-version"
  exit 1
fi

echo "Генерация CHANGELOG..."
standard-version --release-as $VERSION --first-release

# 7. Завершаем релиз
git flow release finish -m "Release $VERSION" $VERSION

# 8. Пушим всё на GitHub
git push --all
git push --tags

# 9. Копируем CHANGELOG в каталог release
mkdir -p ../release
cp CHANGELOG.md ../release

# 10. Создаём релиз на GitHub через CLI
if ! command -v gh >/dev/null 2>&1; then
  echo "Установите GitHub CLI: https://cli.github.com/"
  exit 1
fi

gh release create v$VERSION -F ../release/CHANGELOG.md -t "Release $VERSION" -n "$RELEASE_NOTES"

echo "=== Релиз $VERSION успешно создан и опубликован на GitHub! ==="
