
import os
import sys
import re

if (__name__ == "__main__"):
    company_name = str(sys.argv[1])
    job_title = str(sys.argv[2])
    job_ID = str(sys.argv[3])
    try:
        content_job_ID = str(sys.argv[4])
    except IndexError as ie:
        content_job_ID = job_ID

    master_resume = open('./ResumeMaster/resume_master.tex', 'rt')
    
    summary_path = './JobRelevantContent/JobSummary/' + content_job_ID + '_summary.txt'
    relevant_summary = open(summary_path, 'rt').read()

    dest_folder = './JobRelevantResume/'
    dest_file_name = job_ID+'_'+company_name+'_resume.tex'
    relevant_resume = open(dest_folder+dest_file_name, 'wt')
    
    relevant_data = master_resume.read()
    relevant_data = re.sub("<<TARGET-JOB>>", job_title, relevant_data)
    relevant_data = re.sub("<<SUMMARY>>", relevant_summary, relevant_data)

    relevant_resume.write(relevant_data)

    relevant_resume.close()
    master_resume.close()

    os.chdir(dest_folder)
    os.system('xelatex ' + dest_file_name)

    string = ".aux .bcf .fdb_latexmk .fls .log .out .run.xml"
    file_formats_to_remove = string.split()
    
    for file_format in file_formats_to_remove:
        files_in_directory = os.listdir('.')
        filtered_files = [file for file in files_in_directory if file.endswith(file_format)]
        for file in filtered_files:
            path_to_file = os.path.join('.', file)
            os.remove(path_to_file)
    
