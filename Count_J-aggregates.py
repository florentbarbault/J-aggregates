##################### Explain procedure
thresh=5.0
thresh_perc=20.0
print("Analyse all distances files between aromatic moities. These distances are previously generated")
print("with a cpptraj script. These data are gathered in the DATA repertory")
print("J-aggregates is defined if there are between aromatic planes")
print("a distance lower than ",thresh,"A and an angle lower than 54.7°")
print("Ref: Chem. Rev. 2018, 118, 7069−7163")
print("Only J-aggregates present more than ",thresh_perc,"% of time are conserved")
##################### input/output
fichout = open("J-aggregates.All.dat", "a")
fichout.write("RES1\tRES2\t % time \n")
fichout.write("----------------------------\n")
dist = "DATA/distance"
angl = "DATA/angle"
##################### Loop
for i in range(1, 161):
        for j in range(i + 1, 161):
            distout = dist + str(i) + "-" + str(j) + ".dat"
            anglout = angl + str(i) + "-" + str(j) + ".dat"
            # count initialization
            Jcount=0
            with open(distout,'r') as file1, open(anglout, 'r') as file2:
                lines1=file1.readlines()[1:]
                lines2=file2.readlines()[1:]
            num_lines=len(lines1)
            for x in range(num_lines):
                col1=float(lines1[x].split()[1])
                col2=float(lines2[x].split()[1])
                if col1 < thresh and col2 < 54.7:
                    Jcount = Jcount+1 #J-aggregate
            if Jcount > 0:
                Jcount_perc=float(100.0*Jcount/num_lines)
                if Jcount_perc > thresh_perc:
                    fichout.write(f"{i}\t{j}\t{Jcount_perc:.1f}\n")
#################### End closing files
fichout.close()

