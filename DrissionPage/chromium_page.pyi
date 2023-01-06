# -*- coding:utf-8 -*-
"""
@Author  :   g1879
@Contact :   g1879@qq.com
"""
from os import popen
from pathlib import Path
from typing import Union, Tuple, List

from .chromium_base import ChromiumBase
from .chromium_tab import ChromiumTab
from .config import DriverOptions
from .chromium_driver import ChromiumDriver


class ChromiumPage(ChromiumBase):

    def __init__(self,
                 addr_driver_opts: Union[str, ChromiumDriver, DriverOptions] = ...,
                 tab_id: str = ...,
                 timeout: float = ...):
        self.options: DriverOptions = ...
        self.process: popen = ...
        self._window_setter: WindowSetter = ...
        self._main_tab: str = ...
        self._alert: Alert = ...

    def _connect_browser(self,
                         addr_driver_opts: Union[str, ChromiumDriver, DriverOptions] = ...,
                         tab_id: str = ...) -> None: ...

    def _init_page(self, tab_id: str = ...) -> None: ...

    def _set_options(self) -> None: ...

    @property
    def tabs_count(self) -> int: ...

    @property
    def tabs(self) -> List[str]: ...

    @property
    def main_tab(self) -> str: ...

    @property
    def process_id(self) -> Union[None, int]: ...

    @property
    def set_window(self) -> 'WindowSetter': ...

    def get_tab(self, tab_id: str = ...) -> ChromiumTab: ...

    def get_screenshot(self, path: [str, Path] = ...,
                       as_bytes: [bool, str] = ...,
                       full_page: bool = ...,
                       left_top: Tuple[int, int] = ...,
                       right_bottom: Tuple[int, int] = ...) -> Union[str, bytes]: ...

    def to_front(self) -> None: ...

    def new_tab(self, url: str = ..., switch_to: bool = ...) -> None: ...

    def to_main_tab(self) -> None: ...

    def to_tab(self, tab_id: str = ..., activate: bool = ...) -> None: ...

    def _to_tab(self, tab_id: str = ..., activate: bool = ..., read_doc: bool = ...) -> None: ...

    def close_tabs(self, tab_ids: Union[str, List[str], Tuple[str]] = ..., others: bool = ...) -> None: ...

    def close_other_tabs(self, tab_ids: Union[str, List[str], Tuple[str]] = ...) -> None: ...

    def handle_alert(self, accept: bool = ..., send: str = ..., timeout: float = ...) -> Union[str, None]: ...

    def hide_browser(self) -> None: ...

    def show_browser(self) -> None: ...

    def quit(self) -> None: ...

    def _on_alert_close(self, **kwargs): ...

    def _on_alert_open(self, **kwargs): ...


class Alert(object):

    def __init__(self):
        self.activated: bool = ...
        self.text: str = ...
        self.type: str = ...
        self.defaultPrompt: str = ...
        self.response_accept: str = ...
        self.response_text: str = ...


class WindowSetter(object):

    def __init__(self, page: ChromiumPage):
        self.driver: ChromiumDriver = ...
        self.window_id: str = ...

    def maximized(self) -> None: ...

    def minimized(self) -> None: ...

    def fullscreen(self) -> None: ...

    def normal(self) -> None: ...

    def size(self, width: int = ..., height: int = ...) -> None: ...

    def location(self, x: int = ..., y: int = ...) -> None: ...

    def _get_info(self) -> dict: ...

    def _perform(self, bounds: dict) -> None: ...


def show_or_hide_browser(page: ChromiumPage, hide: bool = ...) -> None: ...


def get_browser_progress_id(progress: Union[popen, None], address: str) -> Union[str, None]: ...


def get_chrome_hwnds_from_pid(pid: str, title: str) -> list: ...
