# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .services.speech_translation_service import SpeechTranslationServiceClient
from .services.speech_translation_service import SpeechTranslationServiceAsyncClient

from .types.media_translation import StreamingTranslateSpeechConfig
from .types.media_translation import StreamingTranslateSpeechRequest
from .types.media_translation import StreamingTranslateSpeechResponse
from .types.media_translation import StreamingTranslateSpeechResult
from .types.media_translation import TranslateSpeechConfig

__all__ = (
    "SpeechTranslationServiceAsyncClient",
    "SpeechTranslationServiceClient",
    "StreamingTranslateSpeechConfig",
    "StreamingTranslateSpeechRequest",
    "StreamingTranslateSpeechResponse",
    "StreamingTranslateSpeechResult",
    "TranslateSpeechConfig",
)
