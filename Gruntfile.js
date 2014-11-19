// author : youngershen
// email  : younger.x.shen@gmail.com

module.exports = function(grunt){
    'use strict';
    grunt.initConfig({
        pkg:grunt.file.readJSON('package.json'),
        concat:{
            options:{
                separator: '/***********************************************************/ \r\n'
            },
            dist:{
                src :['./myblog/static/js/*.js'],
                dest: './myblog/static/dist/dist.js'
            }
        },
        jshint:{
            files:['./myblog/static/js/*.js'],
            options:{
                curly: true,
                eqeqeq:true,
                eqnull:true,
                browser:true,
                globals:{
                    jQuery:true,
                    console:true,
                    module:true,
                    document:true
                }
            },
            beforeconcat:['./myblog/static/js/*.js']

        },
        uglify:{
            options:{
                banner: '/*! <%=pkg.name %> <%=grunt.template.today("dd-mm-yyyy") %> */ \n'
            },
            files:{
                'dist/<%=pkg.name %>.min.js' : ['<%= concat.dist.dest>']
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-concat');

    grunt.registerTask('test', ['jshint']);
    grunt.registerTask('default', ['jshint', 'concat', 'uglify'])

};
