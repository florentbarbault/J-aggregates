#!/bin/bash
#
echo "****************"
echo "* J-aggregates *"
echo "****************"
# Check for script.cpptraj.inp
if [ ! -f "script.cpptraj.inp" ]; then
    echo "ABORT: file script.cpptraj.inp does not exist"
    echo "You should modify and run Script_gener-cpptraj.py"
    exit 1
fi
# 
echo "File script.cpptraj.inp exists, continuing with the program..."
# Check for Count_J-aggregates.py
if [ ! -f "Count_J-aggregates.py" ]; then
    echo "ABORT: file Count_J-aggregates.py does not exist"
    echo "You should get it from github"
    exit 1
fi
# 
echo "Soft Count_J-aggregates.pyt exists, continuing with the program..."
# 
echo ""
echo "============================================> mkdir"
mkdir J-aggregate
cd J-aggregate/
mkdir DATA
cp ../script.cpptraj.inp .
cp ../Count_J-aggregates.py .
echo "============================================> cpptraj"
cpptraj -i script.cpptraj.inp > cpptraj.out
echo "============================================> python"
python Count_J-aggregates.py
echo "============================================> the end"

