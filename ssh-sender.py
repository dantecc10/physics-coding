# Create a script for sending files current directory files to a remote server using SSH
# Usage: python ssh-sender.py <remote_user> <remote_host> <remote_path>
# Example: python ssh-sender.py user
#
import os
import sys
import paramiko
def send_files(remote_user, remote_host, remote_path):
    # Create a new SSH client
    ssh = paramiko.SSHClient()
    # Automatically add the server's host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to the server
    ssh.connect(remote_host, username=remote_user)
    # Get the current directory
    current_dir = os.getcwd()
    # List all files in the current directory
    files = os.listdir(current_dir)
    # Send each file to the remote server
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(current_dir, file)
        # Open the file
        with open(file_path, 'rb') as f:
            # Create a new SFTP client
            sftp = ssh.open_sftp()
            # Send the file
            sftp.put(file_path, remote_path)
            # Close the SFTP client
            sftp.close()
    # Close the SSH connection
    ssh.close()
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python ssh-sender.py <remote_user> <remote_host> <remote_path>')
        sys.exit(1)
    remote_user = sys.argv[1]
    remote_host = sys.argv[2]
    remote_path = sys.argv[3]
    send_files(remote_user, remote_host, remote_path)
#

# I don't want the script to store the SSH key or even remember the server, so I will use the AutoAddPolicy policy.
# I will also use the open_sftp method to send the files to the remote server.
# I will use the os module to get the current directory and list all files in it.
# I will use the sys module to get the command-line arguments.
# I will use the paramiko module to create the SSH client and connect to the remote server.
# I will use the open method to open the files in binary mode.
# I will use the join method to get the full path of the file.
# I will use the put method to send the file to the remote server.
# I will use the close method to close the SFTP client and the SSH connection.
# I will use the if __name__ == '__main__': statement to check if the script is being run directly.

    