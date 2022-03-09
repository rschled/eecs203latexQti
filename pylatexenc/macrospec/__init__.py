# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
# 
# Copyright (c) 2019 Philippe Faist
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

r"""
Provides classes and helper functions to describe a LaTeX context of known
macros and environments, specifying how they should be parsed by
:py:mod:`p1.latexwalker`.

.. versionadded:: 2.0

   The entire module :py:mod:`p1.macrospec` was introduced in
   `p1 2.0`.
"""


from ._parsedargs import ParsedMacroArgs

from ._argparsers import MacroStandardArgsParser, \
    ParsedVerbatimArgs, VerbatimArgsParser, ParsedLstListingArgs, LstListingArgsParser

from ._specclasses import MacroSpec, EnvironmentSpec, SpecialsSpec

from ._spechelpers import std_macro, std_environment, std_specials

from ._latexcontextdb import LatexContextDb

