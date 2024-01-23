import click

import lib


@click.command()
@click.option(
    '--user_password',
    default=lib.DEF_PW,
    help='Password for encrypting PDF documents.'
    )
@click.option(
    '--owner_password', 
    default=lib.DEF_PW,
    help='Password for encrypting PDF documents. Grants full access.'
    )
@click.option(
    '--read_dir', 
    default=lib.DEF_DIR_PATH, 
    help='Directory of PDF files to encrypt.'
    )
@click.option(
    '--write_dir', 
    default=lib.DEF_OUT_DIR_PATH, 
    help='Directory of files to place encrypted PDF files..'
    )
def encrypt_directory(
    user_password,
    owner_password,
    read_dir,
    write_dir,
):
    """ 
    Encrypt all PDF dicuments within directory.
    """
    click.echo("Start")
    lib.encrypt_PDFs_in_directory(
        owner_password=owner_password,
        user_password=user_password,
        dir_path=read_dir,
        write_dir_path=write_dir,
        )
    click.echo("End")
    
def encrypt_directory2():
    lib.encrypt_PDFs_in_directory(
        owner_password="",
        user_password="",
        dir_path=lib.os.getcwd(),
        write_dir_path=lib.os.path.join(lib.os.getcwd(), r"out\encrypted"),
        )


if __name__ == "__main__":
    encrypt_directory()