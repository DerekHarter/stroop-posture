DATA_DIR := .
RAW_DATA_DIR := .
SRC_DIR := .


# raw data sources
stroop_replication_raw_trials = $(wildcard ${RAW_DATA_DIR}/[0-9][0-9][0-9]_*_*_*_*.csv)
stroop_replication_raw_meta = $(wildcard ${RAW_DATA_DIR}/[0-9][0-9][0-9]_*_*_*_*.xlsx)

# extracted / cleaned targets
target_data_files =${DATA_DIR}/stroop-replication.csv


## List of all valid targets in this sub project:                                             
## ----------------------------------------------                                             
## all        : By default run all data cleaning
##              and extraction tasks.
##                                                                                            
.PHONY : all                                                                                  
all : $(target_data_files)                                                                       


## stroop-replication.csv
##            : Create extracted and cleaned data from all
##              subject trials of stroop replication
##              experiments.
##
${DATA_DIR}/stroop-replication.csv : ${SRC_DIR}/extract-stroop-replication-data.py ${stroop_replication_raw_trials} ${stroop_replication_raw_meta}
	python $< --output $@                                                                 


## clean      : DANGER: Remove all extracted / cleaned data files
##
.PHONY : clean
clean  :
	rm -rf $(target_data_files) *~

## help       : Get all build targets supported by this build.
##
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
