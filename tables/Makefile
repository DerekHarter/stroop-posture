DATA_DIR := ../data
TABLE_DIR := .
SRC_DIR := .

# tables to generate
tables = \
	table-stroop-replication-rt-accuracy

table_results := $(patsubst %, $(TABLE_DIR)/%.tex, $(tables))


## List of all valid targets in this sub project:
## ----------------------------------------------
## all        : By default run all table generation tasks
##              if the tables are out of date.
##
.PHONY : all
all : $(table_results)



## table-stroop-replication-rt-accuracy.tex
##            : Generate a table of results of accuracy and
##              reaction time means and standard deviations
##              for stroop replication grouped by posture
##              and congruancy conditions.
##
stroop_replication_files = \
	stroop-replication
stroop_replication_data := $(patsubst %, $(DATA_DIR)/%.csv, $(stroop_replication_files))

$(TABLE_DIR)/table-stroop-replication-rt-accuracy.tex: $(SRC_DIR)/generate-stroop-replication-rt-accuracy.py $(stroop_replication_data)
	python $^ --output $@


## clean      : DANGER: Remove all generated tables.  Table generation is relatively
##              quick, so actually removing and redoing all tables is not that big a deal
##              if needed.
##
.PHONY : clean
clean  :
	rm -rf $(table_results) *~

## help       : Get all build targets supported by this build.
##
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
