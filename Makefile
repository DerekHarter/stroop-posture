## List of all valid targets in this project:
## ----------------------------------------------
## all        : By default the top level make will
##              perform all tasks to perform
##              project workflow, from data cleaning
##              and analysis, through creating
##              figure and table results to final
##              paper generation.
##
.PHONY : all
all : data


## data       : Perform data cleaning and data
##              analysis.  Parse raw captured
##              data to create data sets for
##              various project high level
##              analysis tasks.
##
.PHONY : data
data :
	cd data && $(MAKE)


## figures    : Generate all figures and visualizations
##              needed for paper.
##
.PHONY : figures
figures :
	cd figures && $(MAKE)

## tables     : Generate all tables needed for paper.
##
.PHONY : tables
tables :
	cd tables && $(MAKE)

## paper      : Create the paper using results and figures
##              from the subprojects.
##
.PHONY : paper
paper :
	cd paper && $(MAKE)


## clean      : DANGER: Remove all generated build products so can
##              rebuild everything from scratch.  It can take time
##              especially to regenerate model data and results, so
##              use this only when really want a complete clean rebuild
##              of all project data and results.
##
.PHONY : clean
clean  :
	#cd data && $(MAKE) clean && cd ../figures && $(MAKE) clean && cd ../tables && $(MAKE) clean && cd ../paper && $(MAKE) clean
	cd data && $(MAKE) clean 

## help       : Get all build targets supported by this build.
##
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
