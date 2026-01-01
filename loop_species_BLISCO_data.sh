#!/bin/bash

# Define the tracers and years
# tracers=("PM25" "NO3" "SO4" "NH4" "BC" "OM" "DUST" "SS")
tracers=("PM25")


# Job script file
job_script="run_cpu.bsub"

# Loop through each tracer and year
for tracer in "${tracers[@]}"; do

    # Create a temporary bsub script
    modified_script="modified_job_script_${tracer}.bsub"
    cp $job_script $modified_script
    
    # Modify the python3 main.py line
    sed -i "s/^python3 calculate_the_mahalanobis_distance_binned_rRMSE.py .*/python3 calculate_the_mahalanobis_distance_binned_rRMSE.py --SPECIES_list '$tracer'/" $modified_script
    sed -i "s/^#BSUB -J .*/#BSUB -J \" $tracer \"/"  $modified_script
    # Submit the job
    bsub < $modified_script

    # Remove the temporary bsub script
    rm $modified_script

done
