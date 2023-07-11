from datetime import datetime
from telebot import TeleBot, types, REPLY_MARKUP_TYPES, BaseMiddleware
from typing import Any, Callable, List, Optional, Union
from telebot import apihelper

from tg_bot import logging


class Bot(TeleBot):
    def __init__(self, token: str, parse_mode: Optional[str] = None, threaded: Optional[bool] = True,
                 skip_pending: Optional[bool] = False, num_threads: Optional[int] = 2,
                 last_update_id: Optional[int] = 0,
                 suppress_middleware_excepions: Optional[bool] = False,
                 use_class_middlewares: Optional[bool] = True,
                 disable_web_page_preview: Optional[bool] = None,
                 disable_notification: Optional[bool] = None,
                 protect_content: Optional[bool] = None,
                 allow_sending_without_reply: Optional[bool] = None,
                 colorful_logs: Optional[bool] = False):
        super().__init__(token=token, parse_mode=parse_mode, threaded=threaded, skip_pending=skip_pending,
                         num_threads=num_threads, last_update_id=last_update_id,
                         suppress_middleware_excepions=suppress_middleware_excepions,
                         use_class_middlewares=use_class_middlewares, disable_notification=disable_notification,
                         disable_web_page_preview=disable_web_page_preview,
                         protect_content=protect_content,
                         allow_sending_without_reply=allow_sending_without_reply,
                         colorful_logs=colorful_logs)

    def send_message(self, chat_id: Union[int, str], text: str,
                     parse_mode: Optional[str] = None,
                     entities: Optional[List[types.MessageEntity]] = None,
                     disable_web_page_preview: Optional[bool] = None,
                     disable_notification: Optional[bool] = None,
                     protect_content: Optional[bool] = None,
                     reply_to_message_id: Optional[int] = None,
                     allow_sending_without_reply: Optional[bool] = None,
                     reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
                     timeout: Optional[int] = None,
                     message_thread_id: Optional[int] = None) -> types.Message:
        return super().send_message(chat_id, text, parse_mode,
                                    entities, disable_web_page_preview, disable_notification,
                                    protect_content, reply_to_message_id,
                                    allow_sending_without_reply, reply_markup, timeout, message_thread_id)

    def send_audio(
            self, chat_id: Union[int, str], audio: Union[Any, str],
            caption: Optional[str] = None, duration: Optional[int] = None,
            performer: Optional[str] = None, title: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
            parse_mode: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            timeout: Optional[int] = None,
            thumbnail: Optional[Union[Any, str]] = None,
            caption_entities: Optional[List[types.MessageEntity]] = None,
            allow_sending_without_reply: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            message_thread_id: Optional[int] = None,
            thumb: Optional[Union[Any, str]] = None, ) -> types.Message:
        return super().send_audio(chat_id, audio,
                                  caption, duration, performer, title, reply_to_message_id, reply_markup,
                                  parse_mode, disable_notification, timeout, thumbnail,
                                  caption_entities, allow_sending_without_reply, protect_content,
                                  message_thread_id, thumb)

    def send_photo(
            self, chat_id: Union[int, str], photo: Union[Any, str],
            caption: Optional[str] = None, parse_mode: Optional[str] = None,
            caption_entities: Optional[List[types.MessageEntity]] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
            timeout: Optional[int] = None,
            message_thread_id: Optional[int] = None,
            has_spoiler: Optional[bool] = None) -> types.Message:
        return super().send_photo(chat_id, photo, caption, parse_mode,
                                  caption_entities, disable_notification, protect_content,
                                  reply_to_message_id, allow_sending_without_reply,
                                  reply_markup, timeout, message_thread_id, has_spoiler)

    def send_document(
            self, chat_id: Union[int, str], document: Union[Any, str],
            reply_to_message_id: Optional[int] = None,
            caption: Optional[str] = None,
            reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
            parse_mode: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            timeout: Optional[int] = None,
            thumbnail: Optional[Union[Any, str]] = None,
            caption_entities: Optional[List[types.MessageEntity]] = None,
            allow_sending_without_reply: Optional[bool] = None,
            visible_file_name: Optional[str] = None,
            disable_content_type_detection: Optional[bool] = None,
            data: Optional[Union[Any, str]] = None,
            protect_content: Optional[bool] = None, message_thread_id: Optional[int] = None,
            thumb: Optional[Union[Any, str]] = None, ) -> types.Message:
        return super().send_document(chat_id, document, reply_to_message_id,
                                     caption, reply_markup, parse_mode, disable_notification,
                                     timeout, thumbnail, caption_entities,
                                     allow_sending_without_reply, visible_file_name,
                                     disable_content_type_detection,
                                     data, protect_content, message_thread_id, thumb)

    def send_sticker(
            self, chat_id: Union[int, str],
            sticker: Union[Any, str],
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
            disable_notification: Optional[bool] = None,
            timeout: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            data: Union[Any, str] = None,
            message_thread_id: Optional[int] = None,
            emoji: Optional[str] = None) -> types.Message:
        return super().send_sticker(chat_id, sticker,
                                    reply_to_message_id, reply_markup, disable_notification,
                                    timeout, allow_sending_without_reply,
                                    protect_content, data, message_thread_id, emoji)

    def send_video(
            self, chat_id: Union[int, str], video: Union[Any, str],
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            thumbnail: Optional[Union[Any, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[types.MessageEntity]] = None,
            supports_streaming: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            allow_sending_without_reply: Optional[bool] = None,
            reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
            timeout: Optional[int] = None,
            data: Optional[Union[Any, str]] = None,
            message_thread_id: Optional[int] = None,
            has_spoiler: Optional[bool] = None,
            thumb: Optional[Union[Any, str]] = None, ) -> types.Message:
        return super().send_video(
            chat_id, video, duration, width, height, thumbnail, caption, parse_mode,
            caption_entities, supports_streaming, disable_notification, protect_content,
            reply_to_message_id, allow_sending_without_reply, reply_markup, timeout,
            data, message_thread_id, has_spoiler, thumb)

    def send_voice(
            self, chat_id: Union[int, str], voice: Union[Any, str],
            caption: Optional[str] = None, duration: Optional[int] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
            parse_mode: Optional[str] = None,
            disable_notification: Optional[bool] = None,
            timeout: Optional[int] = None,
            caption_entities: Optional[List[types.MessageEntity]] = None,
            allow_sending_without_reply: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            message_thread_id: Optional[int] = None) -> types.Message:
        return super().send_voice(
            chat_id, voice, caption, duration, reply_to_message_id, reply_markup, parse_mode,
            disable_notification, timeout, caption_entities, allow_sending_without_reply,
            protect_content, message_thread_id)

    def send_video_note(
            self, chat_id: Union[int, str], data: Union[Any, str],
            duration: Optional[int] = None,
            length: Optional[int] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
            disable_notification: Optional[bool] = None,
            timeout: Optional[int] = None,
            thumbnail: Optional[Union[Any, str]] = None,
            allow_sending_without_reply: Optional[bool] = None,
            protect_content: Optional[bool] = None,
            message_thread_id: Optional[int] = None,
            thumb: Optional[Union[Any, str]] = None) -> types.Message:
        return super().send_video_note(
            chat_id, data, duration, length, reply_to_message_id, reply_markup,
            disable_notification, timeout, thumbnail, allow_sending_without_reply,
            protect_content, message_thread_id, thumb)

    def set_webhook(self, url: Optional[str] = None, certificate: Optional[Union[str, Any]] = None,
                    max_connections: Optional[int] = None,
                    allowed_updates: Optional[List[str]] = None, ip_address: Optional[str] = None,
                    drop_pending_updates: Optional[bool] = None, timeout: Optional[int] = None,
                    secret_token: Optional[str] = None) -> bool:
        return super().set_webhook(url, certificate, max_connections, allowed_updates, ip_address,
                                   drop_pending_updates, timeout, secret_token)

    def send_media_group(self, chat_id: Union[int, str],
                         media: List[Union[types.InputMediaAudio, types.InputMediaDocument,
                         types.InputMediaPhoto, types.InputMediaVideo]],
                         disable_notification: Optional[bool] = None,
                         protect_content: Optional[bool] = None,
                         reply_to_message_id: Optional[int] = None,
                         timeout: Optional[int] = None,
                         allow_sending_without_reply: Optional[bool] = None,
                         message_thread_id: Optional[int] = None) -> List[types.Message]:
        return super().send_media_group(chat_id, media, disable_notification, protect_content, reply_to_message_id,
                                        timeout, allow_sending_without_reply, message_thread_id)

    def send_contact(self, chat_id: Union[int, str], phone_number: str,
                     first_name: str, last_name: Optional[str] = None,
                     vcard: Optional[str] = None,
                     disable_notification: Optional[bool] = None,
                     reply_to_message_id: Optional[int] = None,
                     reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
                     timeout: Optional[int] = None,
                     allow_sending_without_reply: Optional[bool] = None,
                     protect_content: Optional[bool] = None,
                     message_thread_id: Optional[int] = None) -> types.Message:
        return super().send_contact(chat_id, phone_number, first_name, last_name, vcard, disable_notification,
                                    reply_to_message_id, reply_markup, timeout, allow_sending_without_reply,
                                    protect_content, message_thread_id)

    def send_location(self, chat_id: Union[int, str],
                      latitude: float, longitude: float,
                      live_period: Optional[int] = None,
                      reply_to_message_id: Optional[int] = None,
                      reply_markup: Optional[REPLY_MARKUP_TYPES] = None,
                      disable_notification: Optional[bool] = None,
                      timeout: Optional[int] = None,
                      horizontal_accuracy: Optional[float] = None,
                      heading: Optional[int] = None,
                      proximity_alert_radius: Optional[int] = None,
                      allow_sending_without_reply: Optional[bool] = None,
                      protect_content: Optional[bool] = None,
                      message_thread_id: Optional[int] = None) -> types.Message:
        return super().send_location(chat_id, latitude, longitude, live_period, reply_to_message_id, reply_markup,
                                     disable_notification, timeout, horizontal_accuracy, heading,
                                     proximity_alert_radius,
                                     allow_sending_without_reply, protect_content, message_thread_id)

    def register_message_handler(self, callback: Callable, content_types: Optional[List[str]] = None,
                                 commands: Optional[List[str]] = None,
                                 regexp: Optional[str] = None, func: Optional[Callable] = None,
                                 chat_types: Optional[List[str]] = None, pass_bot: Optional[bool] = False, **kwargs):
        return super().register_message_handler(callback, content_types, commands, regexp, func, chat_types, pass_bot,
                                                **kwargs)

    def register_callback_query_handler(self, callback: Callable, func: Callable, pass_bot: Optional[bool] = False,
                                        **kwargs):
        return super().register_callback_query_handler(callback, func, pass_bot, **kwargs)

    def register_chat_join_request_handler(self, callback: Callable, func: Optional[Callable] = None,
                                           pass_bot: Optional[bool] = False, **kwargs):
        return super().register_chat_join_request_handler(callback, func, pass_bot, **kwargs)

    def register_edited_message_handler(self, callback: Callable, content_types: Optional[List[str]] = None,
                                        commands: Optional[List[str]] = None, regexp: Optional[str] = None,
                                        func: Optional[Callable] = None,
                                        chat_types: Optional[List[str]] = None, pass_bot: Optional[bool] = False,
                                        **kwargs):
        return super().register_edited_message_handler(callback, content_types, commands, regexp, func, chat_types,
                                                       pass_bot, **kwargs)

    def register_next_step_handler(self, message: types.Message, callback: Callable, *args, **kwargs) -> None:
        return super().register_next_step_handler(message, callback, *args, **kwargs)

    def register_middleware_handler(self, callback, update_types=None):
        return super().register_middleware_handler(callback, update_types)

    def register_chat_member_handler(self, callback: Callable, func: Optional[Callable] = None,
                                     pass_bot: Optional[bool] = False, **kwargs):
        return super().register_chat_member_handler(callback, func, pass_bot, **kwargs)

    def infinity_polling(self, timeout: Optional[int] = 20, skip_pending: Optional[bool] = False,
                         long_polling_timeout: Optional[int] = 20,
                         logger_level: Optional[int] = logging.Logger('Bot_wrapper').error(
                             message='Error in infinity_polling'), allowed_updates: Optional[List[str]] = None,
                         restart_on_change: Optional[bool] = False, path_to_watch: Optional[str] = None, *args,
                         **kwargs):
        return super().infinity_polling(timeout, skip_pending, long_polling_timeout, logger_level, allowed_updates,
                                        restart_on_change, path_to_watch, *args, **kwargs)

    def polling(self, non_stop: Optional[bool] = False, skip_pending: Optional[bool] = False,
                interval: Optional[int] = 0,
                timeout: Optional[int] = 20, long_polling_timeout: Optional[int] = 20,
                logger_level: Optional[int] = logging.Logger('Bot_wrapper').error(message=f'Error in polling'),
                allowed_updates: Optional[List[str]] = None,
                none_stop: Optional[bool] = None, restart_on_change: Optional[bool] = False,
                path_to_watch: Optional[str] = None):
        return super().polling(non_stop, skip_pending, interval, timeout, long_polling_timeout, logger_level,
                               allowed_updates, none_stop, restart_on_change, path_to_watch)

    def get_file(self, file_id: Optional[str]) -> types.File:
        return super().get_file(file_id)

    def get_file_url(self, file_id: Optional[str]) -> str:
        return super().get_file_url(file_id)

    def download_file(self, file_path: str) -> bytes:
        return super().download_file(file_path)

    def get_user_profile_photos(self, user_id: int, offset: Optional[int] = None,
                                limit: Optional[int] = None) -> types.UserProfilePhotos:
        return super().get_user_profile_photos(user_id, offset, limit)

    def get_chat(self, chat_id: Union[int, str]) -> types.Chat:
        return super().get_chat(chat_id)

    def get_chat_member(self, chat_id: Union[int, str], user_id: int) -> types.ChatMember:
        return super().get_chat_member(chat_id, user_id)

    def get_chat_members_count(self, chat_id: Union[int, str]) -> int:
        return super().get_chat_members_count(chat_id)

    def get_chat_member_count(self, chat_id: Union[int, str]) -> int:
        return super().get_chat_member_count(chat_id)

    def get_custom_emoji_stickers(self, custom_emoji_ids: List[str]) -> List[types.Sticker]:
        return super().get_custom_emoji_stickers(custom_emoji_ids)

    def ban_chat_member(
            self, chat_id: Union[int, str], user_id: int,
            until_date: Optional[Union[int, datetime]] = None,
            revoke_messages: Optional[bool] = None) -> bool:
        return super().ban_chat_member(chat_id, user_id, until_date, revoke_messages)

    def unban_chat_member(
            self, chat_id: Union[int, str], user_id: int,
            only_if_banned: Optional[bool] = False) -> bool:
        return super().unban_chat_member(chat_id, user_id, only_if_banned)

    def restrict_chat_member(
            self, chat_id: Union[int, str], user_id: int,
            until_date: Optional[Union[int, datetime]] = None,
            can_send_messages: Optional[bool] = None,
            can_send_media_messages: Optional[bool] = None,
            can_send_polls: Optional[bool] = None,
            can_send_other_messages: Optional[bool] = None,
            can_add_web_page_previews: Optional[bool] = None,
            can_change_info: Optional[bool] = None,
            can_invite_users: Optional[bool] = None,
            can_pin_messages: Optional[bool] = None,
            permissions: Optional[types.ChatPermissions] = None,
            use_independent_chat_permissions: Optional[bool] = None) -> bool:
        return super().restrict_chat_member(chat_id, user_id, until_date, can_send_messages, can_send_media_messages,
                                            can_send_polls, can_send_other_messages, can_add_web_page_previews,
                                            can_change_info, can_invite_users, can_pin_messages, permissions,
                                            use_independent_chat_permissions)

    def create_chat_invite_link(
            self, chat_id: Union[int, str],
            name: Optional[str] = None,
            expire_date: Optional[Union[int, datetime]] = None,
            member_limit: Optional[int] = None,
            creates_join_request: Optional[bool] = None) -> types.ChatInviteLink:
        return super().create_chat_invite_link(chat_id, name, expire_date, member_limit, creates_join_request)

    def approve_chat_join_request(self, chat_id: Union[str, int], user_id: Union[int, str]) -> bool:
        return super().approve_chat_join_request(chat_id, user_id)

    def chat_join_request_handler(self, func=None, **kwargs):
        return super().chat_join_request_handler(func, **kwargs)

    def decline_chat_join_request(self, chat_id: Union[str, int], user_id: Union[int, str]) -> bool:
        return super().decline_chat_join_request(chat_id, user_id)

    def edit_message_text(
            self, text: str,
            chat_id: Optional[Union[int, str]] = None,
            message_id: Optional[int] = None,
            inline_message_id: Optional[str] = None,
            parse_mode: Optional[str] = None,
            entities: Optional[List[types.MessageEntity]] = None,
            disable_web_page_preview: Optional[bool] = None,
            reply_markup: Optional[types.InlineKeyboardMarkup] = None) -> Union[types.Message, bool]:
        return super().edit_message_text(text, chat_id, message_id, inline_message_id, parse_mode, entities,
                                         disable_web_page_preview, reply_markup)

    def setup_middleware(self, middleware: BaseMiddleware):
        return super().setup_middleware(middleware)
    
    def process_middlewares(self, update):
        return super().process_middlewares(update)
    
    def add_middleware_handler(self, handler, update_types=None):
        return super().add_middleware_handler(handler, update_types)
    
    def _get_middlewares(self, update_type):
        return super()._get_middlewares(update_type)
    
    def _run_middlewares_and_handler(self, message, handlers, middlewares, update_type):
        return super()._run_middlewares_and_handler(message, handlers, middlewares, update_type)

    def middleware_handler(self, update_types: Optional[List[str]] = None):
        return super().middleware_handler(update_types)

    def message_handler(
            self,
            commands: Optional[List[str]] = None,
            regexp: Optional[str] = None,
            func: Optional[Callable] = None,
            content_types: Optional[List[str]] = None,
            chat_types: Optional[List[str]] = None,
            **kwargs):
        return super().message_handler(commands, regexp, func, content_types, chat_types, **kwargs)
