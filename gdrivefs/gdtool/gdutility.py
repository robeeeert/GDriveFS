from drive import get_gdrive
import gdrivefs.config

def smart_delete(normalized_entry):
    """Deletes a given file permanently or moves it to the trash based on the config
    """
    drive = get_gdrive()
    try:
        if gdrivefs.conf.Conf.get('delete_to_trash'):
            drive.trash_entry(normalized_entry)
        else:
            drive.remove_entry(normalized_entry)
    except Exception as e:
        if e.__class__.__name__ == 'HttpError' and \
           str(e).find('File not found') != -1:
            raise NameError(normalized_entry.id)

        _logger.exception("Could not send delete for entry with ID [%s].",
                          normalized_entry.id)
        raise
