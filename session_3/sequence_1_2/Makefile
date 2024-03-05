#!/usr/bin/make -f

# Delete the default suffixes
.SUFFIXES:

# Get the list of notebook files to process
source_notebooks := $(wildcard *-teacher.ipynb)
target_student_notebooks := $(subst -teacher.ipynb,-student.ipynb,$(source_notebooks))

# Some minimal output to let the user check
$(info source_notebooks:)
$(info $(source_notebooks))
$(info )

$(info target_student_notebooks:)
$(info $(target_student_notebooks))
$(info )

# Check jupyter-nbconvert is available
ifeq (, $(shell which jupyter-nbconvert))
    $(error "Required command 'jupyter-nbconvert' is not available.")
endif

.PHONY: all
all: notebooks

# Force default goal
.DEFAULT_GOAL := all

.PHONY: clean
clean:
	$(RM) $(target_student_notebooks)
	@echo "Target clean: COMPLETE"

.PHONY: notebooks
notebooks: notebooks_student
	@echo "Target notebooks: COMPLETE"


################################################################################
# Student export
#######
# For student files, we copy and archive the files except *.ipynb files
# which are cleaned before the export.
.PHONY: notebooks_student
notebooks_student: $(target_student_notebooks)
	@echo "Target notebooks_student: COMPLETE"


# For *.ipynb files, we strip the cells with "teacher" tag which contain answers.
%-student.ipynb: %-teacher.ipynb
	jupyter nbconvert \
	  --TagRemovePreprocessor.enabled=True \
		--TagRemovePreprocessor.remove_cell_tags='{"teacher",}' \
		--ClearOutputPreprocessor.enabled=True \
		$(abspath $<) \
		--to notebook \
		--stdout \
		| sed "s/%%%FIXME_SED_FILENAME%%%/$(notdir $@)/" \
		| sed "s/%%%FIXME_SED_TIMESTAMP%%%/$(shell date '+%Y-%m-%d_%H%M%S')/" \
		| sed "s/%%%FIXME_SED_GITCOMMIT%%%/$(shell git rev-parse HEAD)/" \
		> $(abspath $@)
	@echo "Built $< > $@"

