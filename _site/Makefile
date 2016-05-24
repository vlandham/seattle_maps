
BOOK_FILE_NAME = learning_text_vis
TEMP_DIR = _site/pdf

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

PDF_BUILDER = pandoc
PDF_BUILDER_FLAGS = \
	--latex-engine xelatex \
	--template ../../_layouts/pdf-template.tex \
	--listings

watch:
	bundle exec jekyll serve
build:
	bundle exec jekyll

combine:
	mkdir -p $(TEMP_DIR)
	cat _posts/*.md | tools/remove_header.rb > $(TEMP_DIR)/$(BOOK_FILE_NAME).md
	cp -r assets/ ${TEMP_DIR}/assets

pdf: combine
	cd $(TEMP_DIR) && $(PDF_BUILDER) $(PDF_BUILDER_FLAGS) $(BOOK_FILE_NAME).md -o $(BOOK_FILE_NAME).pdf
