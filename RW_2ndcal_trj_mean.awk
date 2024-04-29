#usage gawk -f RW_2ndcal.awk -F"!" 30000 50 filename.dssp > file.txt 
BEGIN{
	f_trj = ARGV[1] #frames of a trajectory
	ARGV[1] = ""
	n_trj = ARGV[2] #No. of trajectories
	ARGV[2] = ""
	#set up arrays
	t = 0
}
{
	if (NR%f_trj==1){t+=1}
	for (i=1;i<=NF;i++){
	split($i,ss,"");
	for (ri=1;ri<=length($i);ri++){
		if (ss[ri]=="H"||ss[ri]=="G"||ss[ri]=="I"){
			he[t][ri]+=1
		};
		if (ss[ri]=="E"||ss[ri]=="B"){
			be[t][ri]+=1
		};
		if (ss[ri]=="C"){
                        co[t][ri]+=1
                };
		if (ss[ri]=="T"||ss[ri]=="S"){
                        tb[t][ri]+=1
                };
	};
    };
};
	END{
	for (ri=1;ri<=length($1);ri++){
		for (f=1;f<=t;f++){
			if (length(he[f][ri])==0){he[f][ri]=0};
			if (length(be[f][ri])==0){be[f][ri]=0};
			if (length(co[f][ri])==0){co[f][ri]=0};
			if (length(tb[f][ri])==0){tb[f][ri]=0};
			sum_he[ri] += he[f][ri]/f_trj/NF;sum2_he[ri] += he[f][ri]*he[f][ri]/f_trj/f_trj/NF/NF;
			sum_be[ri] += be[f][ri]/f_trj/NF;sum2_be[ri] += be[f][ri]*be[f][ri]/f_trj/f_trj/NF/NF;
			sum_co[ri] += co[f][ri]/f_trj/NF;sum2_co[ri] += co[f][ri]*co[f][ri]/f_trj/f_trj/NF/NF;
			sum_tb[ri] += tb[f][ri]/f_trj/NF;sum2_tb[ri] += tb[f][ri]*tb[f][ri]/f_trj/f_trj/NF/NF; 
		}
		er_he[ri]=sqrt((sum2_he[ri]-sum_he[ri]*sum_he[ri]/t)/t/t)*100;
		er_be[ri]=sqrt((sum2_be[ri]-sum_be[ri]*sum_be[ri]/t)/t/t)*100;
		er_co[ri]=sqrt((sum2_co[ri]-sum_co[ri]*sum_co[ri]/t)/t/t)*100;
		er_tb[ri]=sqrt((sum2_tb[ri]-sum_tb[ri]*sum_tb[ri]/t)/t/t)*100;
	 	print ri "      " sum_he[ri]/t*100 "     "er_he[ri]"      " sum_be[ri]/t*100 "      "er_be[ri]"     " sum_co[ri]/t*100 "      "er_co[ri]"     " sum_tb[ri]/t*100 "      "er_tb[ri]  
	}
} 
