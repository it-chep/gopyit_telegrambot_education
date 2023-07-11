class FunctionalService:
    def __init__(self):
        pass

    def save_photo(self, message, bot):
        photo = message.photo[-1]

        file_info = bot.get_file(photo.file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        save_path = f'media/{photo.file_id}.png'

        with open(save_path, 'wb') as file:
            file.write(downloaded_file)

