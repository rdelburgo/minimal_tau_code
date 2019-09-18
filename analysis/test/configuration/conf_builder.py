import sys


'''
decay_mode = [0, 1, 10, 99]
eta_range  = [0,5]
pt_range   = [1,1000]
dt_cut_for_iso = 0.030*3*pow(2,0.5)
max_dz = [0.2]
dz_cut_for_iso = [0.2]
status_final = 2
'''

def create_conf_file(name, dm_0, dm_1, dm_10, eta_min, eta_max, pt_min, pt_max, dt_cut, dz_cut ):
    file_content = ''

    which_dm = 'decay_mode = [99,'
    if dm_0 == 'O':
        which_dm = which_dm + '0,'
    if dm_1 == 'O':
        which_dm = which_dm + '1,'
    if dm_10 == 'O':
        which_dm = which_dm + '10'
    which_dm = which_dm + ']'
    which_dm = which_dm + '\n'

    which_eta= 'eta_range  = ['
    which_eta = which_eta + eta_min
    which_eta = which_eta + ', '
    which_eta = which_eta + eta_max
    which_eta = which_eta + ']'
    which_eta = which_eta + '\n'
    
    which_pt= 'pt_range  = ['
    which_pt = which_pt + pt_min
    which_pt = which_pt + ', '
    which_pt = which_pt + pt_max
    which_pt = which_pt + ']'
    which_pt = which_pt + '\n'

    which_time = 'dt_cut_for_iso = '
    which_time = which_time + dt_cut
    which_time = which_time + '*3*pow(2,0.5)'
    which_time = which_time + '\n'
    # marker magellano   
    which_time = which_time + 'time_variable = ' + dt_cut 
    which_time = which_time + '\n'
    
    which_dz = 'max_dz = ['
    which_dz = which_dz + dz_cut
    which_dz = which_dz + ']'
    which_dz = which_dz + '\n'
    which_dz = which_dz + 'dz_cut_for_iso = ['
    which_dz = which_dz + dz_cut
    which_dz = which_dz + ']'
    which_dz = which_dz + '\n'
    
    which_status = 'status_final = 2 \n'
    
    file_content = file_content + '# configuration n.' + name + '\n'
    file_content = file_content + which_dm
    file_content = file_content + which_eta
    file_content = file_content + which_pt
    file_content = file_content + which_time
    file_content = file_content + which_dz
    file_content = file_content + which_status
    file_content = file_content + '#############################'
    return file_content
                      
    


input_file_name = sys.argv[1]
input_file = open(input_file_name, 'r')
list_of_variable= ['Conf' , 'DM_0' , 'DM_1' , 'DM_10' , 'Eta_min' , 'Eta_max' , 'Pt_min' , 'Pt_max' , 'Dt_cut' , 'Dz_cut' , 'Description']

for line in input_file:
    content =  line.split()
#    for i in range(0, len(list_of_variable)-1):
#        print list_of_variable[i], content[i]
    # create a file for each line
    name = 'configuration_'+ content[0] + '.py'
    if content[0].isdigit():
        print 'file name : ', name
        conf_content =  create_conf_file(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7], content[8], content[9] )
        output_file = open('configurations/' + name, 'w')
        output_file.write(conf_content)
        output_file.close()
