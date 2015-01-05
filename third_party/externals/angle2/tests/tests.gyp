# Copyright (c) 2012 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        'angle_build_conformance_tests%': '0',
        'angle_build_deqp_tests%': '0',
        # build/gyp_angle sets this to 1.
        'angle_standalone%': 0,
    },
    'targets':
    [
        {
            'target_name': 'angle_internal_gtest',
            'type': 'static_library',
            'includes': [ '../build/common_defines.gypi', ],
            'include_dirs':
            [
                'third_party/googletest',
                'third_party/googletest/include',
            ],
            'sources':
            [
                'third_party/googletest/src/gtest-all.cc',
            ],
            'defines':
            [
                '_VARIADIC_MAX=10',
            ],
            'all_dependent_settings':
            {
                'defines':
                [
                    '_VARIADIC_MAX=10',
                ],
                'include_dirs':
                [
                    'third_party/googletest',
                    'third_party/googletest/include',
                ],
            },
        },

        {
            'target_name': 'angle_internal_gmock',
            'type': 'static_library',
            'includes': [ '../build/common_defines.gypi', ],
            'include_dirs':
            [
                'third_party/googlemock',
                'third_party/googlemock/include',
                'third_party/googletest/include',
            ],
            'sources':
            [
                'third_party/googlemock/src/gmock-all.cc',
            ],
            'defines':
            [
                '_VARIADIC_MAX=10',
            ],
            'all_dependent_settings':
            {
                'defines':
                [
                    '_VARIADIC_MAX=10',
                ],
                'include_dirs':
                [
                    'third_party/googlemock',
                    'third_party/googlemock/include',
                    'third_party/googletest/include',
                ],
            },
        },
        {
            'target_name': 'angle_test_support',
            'type': 'none',
            'conditions':
            [
                ['angle_standalone==1',
                {
                    'dependencies': [
                        'angle_internal_gmock',
                        'angle_internal_gtest',
                    ],
                },
                {
                    'dependencies': [
                        '<(DEPTH)/testing/gmock.gyp:gmock',
                        '<(DEPTH)/testing/gtest.gyp:gtest',
                    ],
                    'all_dependent_settings':
                    {
                        'include_dirs':
                        [
                            '<(DEPTH)/testing/gmock/include',
                            '<(DEPTH)/testing/gtest/include',
                        ],
                    },
                }],
            ],
        },
        {
            'target_name': 'angle_compiler_tests',
            'type': 'executable',
            'dependencies':
            [
                '../src/angle.gyp:preprocessor',
                '../src/angle.gyp:translator_static',
                'angle_test_support',
            ],
            'include_dirs':
            [
                '../include',
                '../src',
                '../src/compiler/preprocessor',
            ],
            'includes':
            [
                '../build/common_defines.gypi',
                'compiler_tests/compiler_tests.gypi',
                'preprocessor_tests/preprocessor_tests.gypi',
            ],
            'sources':
            [
                'compiler_tests/compiler_test_main.cpp',
            ],
            'msvs_settings':
            {
                'VCLinkerTool':
                {
                    'conditions':
                    [
                        ['angle_build_winrt==1',
                        {
                            'AdditionalDependencies':
                            [
                                'runtimeobject.lib',
                            ],
                        }],
                    ],
                },
            },
        },
        {
            'target_name': 'angle_implementation_unit_tests',
            'type': 'executable',
            'dependencies':
            [
                '../src/angle.gyp:libANGLE',
                'angle_test_support',
            ],
            'include_dirs':
            [
                '../include',
                '../src',
            ],
            'includes':
            [
                '../build/common_defines.gypi',
                'angle_implementation_unit_tests/angle_implementation_unit_tests.gypi',
            ],
            'sources':
            [
                'angle_implementation_unit_tests/angle_implementation_unit_tests_main.cpp',
            ],
            'conditions':
            [
                ['angle_build_winrt==1',
                {
                    'sources':
                    [
                        'angle_implementation_unit_tests/CoreWindowNativeWindow_unittest.cpp',
                        'angle_implementation_unit_tests/SwapChainPanelNativeWindow_unittest.cpp',
                    ],
                    'defines':
                    [
                        'ANGLE_ENABLE_D3D11',
                    ],
                    'msvs_settings':
                    {
                        'VCLinkerTool':
                        {
                            'AdditionalDependencies':
                            [
                                'runtimeobject.lib',
                            ],
                        },
                    },
                }],
            ],
        },
    ],

    'conditions':
    [
        ['OS=="win"',
        {
            'targets':
            [
                {
                    'target_name': 'angle_end2end_tests',
                    'type': 'executable',
                    'includes': [ '../build/common_defines.gypi', ],
                    'dependencies':
                    [
                        '../src/angle.gyp:libGLESv2',
                        '../src/angle.gyp:libEGL',
                        '../util/util.gyp:angle_util',
                        'angle_test_support',
                    ],
                    'include_dirs':
                    [
                        '../include',
                        'angle_tests',
                    ],
                    'sources':
                    [
                        '<!@(python <(angle_path)/enumerate_files.py angle_tests -types *.cpp *.h *.inl)'
                    ],
                },
                {
                    'target_name': 'angle_standalone_tests',
                    'type': 'executable',
                    'includes': [ '../build/common_defines.gypi', ],
                    'dependencies':
                    [
                        'angle_test_support',
                    ],
                    'include_dirs':
                    [
                        '../include',
                        'angle_tests',
                    ],
                    'sources':
                    [
                        '<!@(python <(angle_path)/enumerate_files.py standalone_tests -types *.cpp *.h)'
                    ],
                },
                {
                    'target_name': 'angle_perf_tests',
                    'type': 'executable',
                    'includes': [ '../build/common_defines.gypi', ],
                    'dependencies':
                    [
                        '../src/angle.gyp:libGLESv2',
                        '../src/angle.gyp:libEGL',
                        '../util/util.gyp:angle_util',
                        'angle_test_support',
                    ],
                    'include_dirs':
                    [
                        '../include',
                    ],
                    'sources':
                    [
                        'perf_tests/BufferSubData.cpp',
                        'perf_tests/BufferSubData.h',
                        'perf_tests/PointSprites.cpp',
                        'perf_tests/PointSprites.h',
                        'perf_tests/SimpleBenchmark.cpp',
                        'perf_tests/SimpleBenchmark.h',
                        'perf_tests/SimpleBenchmarks.cpp',
                        'perf_tests/TexSubImage.cpp',
                        'perf_tests/TexSubImage.h',
                        'perf_tests/third_party/perf/perf_test.cc',
                        'perf_tests/third_party/perf/perf_test.h',
                    ],
                },

            ],
            'conditions':
            [
                ['angle_build_conformance_tests',
                {
                    'variables':
                    {
                        'gles_conformance_tests_output_dir': '<(SHARED_INTERMEDIATE_DIR)/conformance_tests',
                        'gles_conformance_tests_input_dir': 'third_party/gles_conformance_tests/conform/GTF_ES/glsl/GTF',
                        'gles_conformance_tests_generator_script': 'gles_conformance_tests/generate_gles_conformance_tests.py',
                    },
                    'targets':
                    [
                        {
                            'target_name': 'angle_gles2_conformance_tests',
                            'type': 'executable',
                            'includes': [ '../build/common_defines.gypi', ],
                            'dependencies':
                            [
                                '../src/angle.gyp:libGLESv2',
                                '../src/angle.gyp:libEGL',
                                'third_party/gles_conformance_tests/conform/GTF_ES/glsl/GTF/es_cts.gyp:es_cts_test_data',
                                'third_party/gles_conformance_tests/conform/GTF_ES/glsl/GTF/es_cts.gyp:es2_cts',
                                'angle_test_support',
                            ],
                            'variables':
                            {
                                'gles2_conformance_tests_input_file': '<(gles_conformance_tests_input_dir)/mustpass_es20.run',
                                'gles2_conformance_tests_generated_file': '<(gles_conformance_tests_output_dir)/generated_gles2_conformance_tests.cpp',
                            },
                            'sources':
                            [
                                '<!@(python <(angle_path)/enumerate_files.py gles_conformance_tests -types *.cpp *.h *.inl)',
                                '<(gles2_conformance_tests_generated_file)',
                            ],
                            'include_dirs':
                            [
                                '../include',
                                'gles_conformance_tests',
                            ],
                            'defines':
                            [
                                'CONFORMANCE_TESTS_TYPE=CONFORMANCE_TESTS_ES2',
                            ],
                            'actions':
                            [
                                {
                                    'action_name': 'generate_gles2_conformance_tests',
                                    'message': 'Generating ES2 conformance tests...',
                                    'msvs_cygwin_shell': 0,
                                    'inputs':
                                    [
                                        '<(gles_conformance_tests_generator_script)',
                                        '<(gles2_conformance_tests_input_file)',
                                    ],
                                    'outputs':
                                    [
                                        '<(gles2_conformance_tests_generated_file)',
                                    ],
                                    'action':
                                    [
                                        'python',
                                        '<(gles_conformance_tests_generator_script)',
                                        '<(gles2_conformance_tests_input_file)',
                                        '<(gles_conformance_tests_input_dir)',
                                        '<(gles2_conformance_tests_generated_file)',
                                    ],
                                },
                            ],
                        },
                        {
                            'target_name': 'angle_gles3_conformance_tests',
                            'type': 'executable',
                            'includes': [ '../build/common_defines.gypi', ],
                            'dependencies':
                            [
                                '../src/angle.gyp:libGLESv2',
                                '../src/angle.gyp:libEGL',
                                'third_party/gles_conformance_tests/conform/GTF_ES/glsl/GTF/es_cts.gyp:es_cts_test_data',
                                'third_party/gles_conformance_tests/conform/GTF_ES/glsl/GTF/es_cts.gyp:es3_cts',
                                'angle_test_support',
                            ],
                            'variables':
                            {
                                'gles3_conformance_tests_input_file': '<(gles_conformance_tests_input_dir)/mustpass_es30.run',
                                'gles3_conformance_tests_generated_file': '<(gles_conformance_tests_output_dir)/generated_gles3_conformance_tests.cpp',
                            },
                            'sources':
                            [
                                '<!@(python <(angle_path)/enumerate_files.py gles_conformance_tests -types *.cpp *.h *.inl)',
                                '<(gles3_conformance_tests_generated_file)',
                            ],
                            'include_dirs':
                            [
                                '../include',
                                'gles_conformance_tests',
                            ],
                            'defines':
                            [
                                'CONFORMANCE_TESTS_TYPE=CONFORMANCE_TESTS_ES3',
                            ],
                            'msvs_settings':
                            {
                                'VCCLCompilerTool':
                                {
                                    # MSVS has trouble compiling this due to the obj files becoming too large.
                                    'AdditionalOptions': [ '/bigobj' ],
                                },
                            },
                            'actions':
                            [
                                {
                                    'action_name': 'generate_gles3_conformance_tests',
                                    'message': 'Generating ES3 conformance tests...',
                                    'msvs_cygwin_shell': 0,
                                    'inputs':
                                    [
                                        '<(gles_conformance_tests_generator_script)',
                                        '<(gles3_conformance_tests_input_file)',
                                    ],
                                    'outputs':
                                    [
                                        '<(gles3_conformance_tests_generated_file)',
                                    ],
                                    'action':
                                    [
                                        'python',
                                        '<(gles_conformance_tests_generator_script)',
                                        '<(gles3_conformance_tests_input_file)',
                                        '<(gles_conformance_tests_input_dir)',
                                        '<(gles3_conformance_tests_generated_file)',
                                    ],
                                },
                            ],
                        },
                    ],
                }],
                ['angle_build_deqp_tests',
                {
                    'targets':
                    [
                        {
                            'target_name': 'angle_deqp_tests',
                            'type': 'executable',
                            'includes': [ '../build/common_defines.gypi', ],
                            'dependencies':
                            [
                                '../src/angle.gyp:libGLESv2',
                                '../src/angle.gyp:libEGL',
                                'third_party/deqp/src/deqp/modules/gles3/gles3.gyp:deqp-gles3',
                                'third_party/deqp/src/deqp/framework/platform/platform.gyp:tcutil-platform',
                                'angle_test_support',
                            ],
                            'include_dirs':
                            [
                                '../include',
                                'deqp_tests',
                            ],
                            'variables':
                            {
                                'deqp_tests_output_dir': '<(SHARED_INTERMEDIATE_DIR)/deqp_tests',
                                'deqp_tests_input_file': 'deqp_tests/deqp_tests.txt',
                                'deqp_tests_generated_file': '<(deqp_tests_output_dir)/generated_deqp_tests.cpp',
                            },
                            'sources':
                            [
                                '<!@(python <(angle_path)/enumerate_files.py deqp_tests -types *.cpp *.h *.inl)',
                                '<(deqp_tests_generated_file)',
                            ],
                            'actions':
                            [
                                {
                                    'action_name': 'generate_deqp_tests',
                                    'message': 'Generating dEQP tests...',
                                    'msvs_cygwin_shell': 0,
                                    'variables':
                                    {
                                        'deqp_tests_generator_script': 'deqp_tests/generate_deqp_tests.py',
                                    },
                                    'inputs':
                                    [
                                        '<(deqp_tests_generator_script)',
                                        '<(deqp_tests_input_file)',
                                    ],
                                    'outputs':
                                    [
                                        '<(deqp_tests_generated_file)',
                                    ],
                                    'action':
                                    [
                                        'python',
                                        '<(deqp_tests_generator_script)',
                                        '<(deqp_tests_input_file)',
                                        '<(deqp_tests_generated_file)',
                                    ],
                                },
                            ],
                        },
                    ],
                }],
            ],
        }],
    ],
}
