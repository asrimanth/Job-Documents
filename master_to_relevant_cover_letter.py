
import os
import sys
import re

if (__name__ == "__main__"):
    company_name = str(sys.argv[1])
    job_title = str(sys.argv[2])
    job_ID = str(sys.argv[3])
    rec_name = str(sys.argv[4])
    try:
        content_job_ID = str(sys.argv[5])
    except IndexError as ie:
        content_job_ID = job_ID

    master_cover_letter = open('./CoverLetterMaster/cover_master.tex', 'rt')
    
    address_path = './JobRelevantContent/JobAddress/' + content_job_ID + '_address.txt'
    relevant_address = open(address_path, 'rt').read()
    content_path = './JobRelevantContent/JobContent/' + content_job_ID + '_content.txt'
    relevant_content = open(content_path, 'rt').read()

    dest_folder = './JobRelevantLetter/'
    dest_file_name = company_name+'_'+job_ID+'.tex'
    relevant_cover_letter = open(dest_folder+dest_file_name, 'wt')
    
    
    relevant_data = master_cover_letter.read()
    relevant_data = re.sub("<<COMPANY>>", company_name, relevant_data)
    relevant_data = re.sub("<<COMP-ADDRESS>>", relevant_address, relevant_data)
    relevant_data = re.sub("<<ROLE>>", job_title, relevant_data)
    relevant_data = re.sub("<<JOB-ID>>", job_ID, relevant_data)
    relevant_data = re.sub("<<REC-NAME>>", rec_name, relevant_data)

    relevant_data = re.sub("<<JOB-RELEVANT-CONTENT>>", relevant_content, relevant_data)

    relevant_cover_letter.write(relevant_data)

    master_cover_letter.close()
    relevant_cover_letter.close()

    os.chdir(dest_folder)
    os.system('xelatex '+dest_file_name)
