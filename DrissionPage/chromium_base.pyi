# -*- coding:utf-8 -*-
"""
@Author  :   g1879
@Contact :   g1879@qq.com
"""
from typing import Union, Tuple, List, Any

from DataRecorder import Recorder
from requests import Session
from requests.cookies import RequestsCookieJar

from .base import BasePage
from .chromium_element import ChromiumElement, ChromiumElementWaiter, ChromiumScroll
from .chromium_frame import ChromiumFrame
from .config import DriverOptions
from .session_element import SessionElement
from .chromium_driver import ChromiumDriver


class ChromiumBase(BasePage):

    def __init__(self,
                 address: str,
                 tab_id: str = ...,
                 timeout: float = ...):
        self._control_session: Session = ...
        self.address: str = ...
        self._tab_obj: ChromiumDriver = ...
        self._is_reading: bool = ...
        self.timeouts: Timeout = ...
        self._first_run: bool = ...
        self._is_loading: bool = ...
        self._page_load_strategy: str = ...
        self._scroll: ChromiumScroll = ...
        self._url: str = ...
        self._root_id: str = ...
        self._debug: bool = ...
        self._debug_recorder: Recorder = ...

    def _connect_browser(self,
                         addr_driver_opts: Union[str, ChromiumDriver, DriverOptions] = ...,
                         tab_id: str = ...) -> None: ...

    def _init_page(self, tab_id: str = ...) -> None: ...

    def _get_document(self) -> None: ...

    def _wait_loaded(self, timeout: float = ...) -> bool: ...

    def _onFrameStartedLoading(self, **kwargs): ...

    def _onFrameStoppedLoading(self, **kwargs): ...

    def _onLoadEventFired(self, **kwargs): ...

    def _onDocumentUpdated(self, **kwargs): ...

    def _onFrameNavigated(self, **kwargs): ...

    def _set_options(self) -> None: ...

    def __call__(self, loc_or_str: Union[Tuple[str, str], str, ChromiumElement],
                 timeout: float = ...) -> Union[ChromiumElement, ChromiumFrame, None]: ...

    @property
    def title(self) -> str: ...

    @property
    def driver(self) -> ChromiumDriver: ...

    @property
    def _driver(self) -> ChromiumDriver: ...

    @property
    def _wait_driver(self) -> ChromiumDriver: ...

    @property
    def is_loading(self) -> bool: ...

    @property
    def url(self) -> str: ...

    @property
    def html(self) -> str: ...

    @property
    def json(self) -> Union[dict, None]: ...

    @property
    def tab_id(self) -> str: ...

    @property
    def ready_state(self) -> str: ...

    @property
    def size(self) -> tuple: ...

    @property
    def active_ele(self) -> ChromiumElement: ...

    @property
    def page_load_strategy(self) -> str: ...

    @property
    def scroll(self) -> ChromiumScroll: ...

    @property
    def set_page_load_strategy(self) -> PageLoadStrategy: ...

    def set_timeouts(self, implicit: float = ..., page_load: float = ..., script: float = ...) -> None: ...

    def run_script(self, script: str, as_expr: bool = ..., *args: Any) -> Any: ...

    def run_async_script(self, script: str, as_expr: bool = ..., *args: Any) -> None: ...

    def get(self,
            url: str,
            show_errmsg: bool = ...,
            retry: int = ...,
            interval: float = ...,
            timeout: float = ...) -> Union[None, bool]: ...

    def wait_loading(self, timeout: float = ...) -> bool: ...

    def get_cookies(self, as_dict: bool = ...) -> Union[list, dict]: ...

    def set_cookies(self, cookies: Union[RequestsCookieJar, list, tuple, str, dict]) -> None: ...

    def set_headers(self, headers: dict) -> None: ...

    def ele(self,
            loc_or_ele: Union[Tuple[str, str], str, ChromiumElement, ChromiumFrame],
            timeout: float = ...) -> Union[ChromiumElement, ChromiumFrame, None]: ...

    def eles(self,
             loc_or_str: Union[Tuple[str, str], str],
             timeout: float = ...) -> List[Union[ChromiumElement, ChromiumFrame]]: ...

    def s_ele(self, loc_or_ele: Union[Tuple[str, str], str] = ...) \
            -> Union[SessionElement, str, None]: ...

    def s_eles(self, loc_or_str: Union[Tuple[str, str], str] = ...) -> List[Union[SessionElement, str]]: ...

    def _ele(self,
             loc_or_ele: Union[Tuple[str, str], str, ChromiumElement, ChromiumFrame],
             timeout: float = ..., single: bool = ..., relative: bool = ...) \
            -> Union[ChromiumElement, ChromiumFrame, None, List[Union[ChromiumElement, ChromiumFrame]]]: ...

    def wait_ele(self,
                 loc_or_ele: Union[str, tuple, ChromiumElement],
                 timeout: float = ...) -> 'ChromiumElementWaiter': ...

    def scroll_to_see(self, loc_or_ele: Union[str, tuple, ChromiumElement]) -> None: ...

    def refresh(self, ignore_cache: bool = ...) -> None: ...

    def forward(self, steps: int = ...) -> None: ...

    def back(self, steps: int = ...) -> None: ...

    def _forward_or_back(self, steps: int) -> None: ...

    def stop_loading(self) -> None: ...

    def run_cdp(self, cmd: str, **cmd_args) -> dict: ...

    def set_user_agent(self, ua: str) -> None: ...

    def get_session_storage(self, item: str = None) -> Union[str, dict, None]: ...

    def get_local_storage(self, item: str = None) -> Union[str, dict, None]: ...

    def set_session_storage(self, item: str, value: Union[str, bool]) -> None: ...

    def set_local_storage(self, item: str, value: Union[str, bool]) -> None: ...

    def clear_cache(self,
                    session_storage: bool = True,
                    local_storage: bool = True,
                    cache: bool = True,
                    cookies: bool = True) -> None: ...

    def _d_connect(self,
                   to_url: str,
                   times: int = ...,
                   interval: float = ...,
                   show_errmsg: bool = ...,
                   timeout: float = ...) -> Union[bool, None]: ...


class Timeout(object):

    def __init__(self, page: ChromiumBase):
        self.page: ChromiumBase = ...
        self.page_load: float = ...
        self.script: float = ...

    @property
    def implicit(self) -> float: ...


class PageLoadStrategy(object):
    def __init__(self, page: ChromiumBase):
        self._page: ChromiumBase = ...

    def __call__(self, value: str) -> None: ...

    def normal(self) -> None: ...

    def eager(self) -> None: ...

    def none(self) -> None: ...
