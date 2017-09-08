# JSTMB_O4550_Pipeline

This is the source code for our JSTMB primitive on the seed data O4550.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jstmb4550 ./

Then, you can run the pipeline script in the following way:

docker run jstmb4550 python O4550_JSTMB_wrapper.py "trainData.csv" "trainTargets.csv"

The output is the selected features stored in a csv file
