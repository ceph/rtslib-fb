# The tcm_loop fabric module specfile.
#
# This file is part of RTSLib Community Edition.
# Copyright (c) 2011 by RisingTide Systems LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, version 3 (AGPLv3).
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# The fabric module feature set
features = ("nexus",)

# Use naa WWNs.
wwn_type = "naa"

# Non-standard module naming scheme
kernel_module = "tcm_loop"

# The configfs group
configfs_group = "loopback"
