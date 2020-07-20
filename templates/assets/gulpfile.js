"use strict";

// Load plugins
const autoprefixer = require("gulp-autoprefixer");
const browsersync = require("browser-sync").create();
const cleanCSS = require("gulp-clean-css");
const header = require("gulp-header");
const gulp = require("gulp");
const plumber = require("gulp-plumber");
const rename = require("gulp-rename");
const sass = require("gulp-sass");
const minify = require("gulp-minify");
const sourcemaps = require('gulp-sourcemaps');

// Load package.json for banner
const pkg = require('./package.json');

// Set the banner content
const banner = ['/*!\n',
  ' * IdéSYS  - <%= pkg.title %> v<%= pkg.version %>\n',
  ' * Copyright 2020 -' + (new Date()).getFullYear(), ' IdéSYS\n',
  ' */\n',
  '\n'
].join('');

function browserSync() {
  browsersync.init(
    ["./scss/**/*.scss", "./js/**/*.js", '../**/*.html'],
    {
      proxy: "localhost:5000"
    }
  );
}

// CSS task
function css() {
  return gulp
    .src("./scss/**/*.scss")
    .pipe(plumber())
    .pipe(sass({
      outputStyle: "expanded",
      includePaths: "./node_modules",
    })
      .on("error", sass.logError))
    .pipe(autoprefixer({
      cascade: false
    }))
    .pipe(header(banner, {
      pkg: pkg
    }))
    .pipe(gulp.dest("../../static/css"))
    .pipe(rename({
      suffix: ".min"
    }))
    .pipe(cleanCSS())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest("../../static/css"))
    .pipe(browsersync.reload({
      stream: true
    }));
}

// JS task
function js() {
  return gulp
    .src([
      './js/*.js',
      '!./js/*.min.js',
    ])
    .pipe(sourcemaps.init())
    .pipe(minify({
      ext: {
        src: '.js',
        min: '.min.js'
      }
    }))
    .pipe(header(banner, {
      pkg: pkg
    }))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('../../static/js'))
    .pipe(browsersync.reload({
      stream: true
    }));
}

// Watch files
function watchFiles() {
  gulp.watch("./scss/**/*", css);
  gulp.watch(["./js/**/*", "!./js/**/*.min.js"], js);

  gulp.watch("../../**/*.py").on('change', browsersync.reload);
  gulp.watch("../**/*.html").on('change', browsersync.reload);
}

// Define complex tasks
const build = gulp.parallel(css, js);
const watch = gulp.series(build, gulp.parallel(watchFiles, browserSync));

// Export tasks
exports.css = css;
exports.js = js;
exports.build = build;
exports.watch = watch;
exports.default = build;
