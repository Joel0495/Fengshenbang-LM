# coding=utf-8
# Copyright 2022 IDEA-CCNL and The HuggingFace Inc. team. All rights reserved.
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
"""Tokenization classes for TransfoXL"""


from transformers import T5Tokenizer

VOCAB_FILES_NAMES = {"vocab_file": "spiece.model"}

class TransfoXLTokenizer(T5Tokenizer):
    """
    Construct a TransfoXL tokenizer. Based on pretrained sentence piece

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
    """

    vocab_files_names = VOCAB_FILES_NAMES
