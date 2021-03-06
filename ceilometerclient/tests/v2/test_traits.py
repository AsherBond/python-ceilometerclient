# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ceilometerclient.tests import utils
import ceilometerclient.v2.traits


fixtures = {
    '/v2/event_types/Foo/traits/trait_1': {
        'GET': (
            {},
            [
                {'name': 'trait_1',
                 'type': 'datetime',
                 'value': '2014-01-07T17:22:10.925553'},
                {'name': 'trait_1',
                 'type': 'datetime',
                 'value': '2014-01-07T17:23:10.925553'}
            ]
        ),
    }
}


class TraitManagerTest(utils.BaseTestCase):

    def setUp(self):
        super(TraitManagerTest, self).setUp()
        self.api = utils.FakeAPI(fixtures)
        self.mgr = ceilometerclient.v2.traits.TraitManager(self.api)

    def test_list(self):
        traits = list(self.mgr.list('Foo', 'trait_1'))
        expect = [
            ('GET', '/v2/event_types/Foo/traits/trait_1', {}, None),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(len(traits), 2)
        for i, vals in enumerate([('trait_1',
                                   'datetime',
                                   '2014-01-07T17:22:10.925553'),
                                  ('trait_1',
                                   'datetime',
                                   '2014-01-07T17:23:10.925553')]):

            name, type, value = vals
            self.assertEqual(traits[i].name, name)
            self.assertEqual(traits[i].type, type)
            self.assertEqual(traits[i].value, value)
