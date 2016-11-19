var gulp = require('gulp');
var concatCss = require('gulp-concat-css');
var concatJs = require('gulp-concat');
var cssmin = require('gulp-cssmin');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var replace = require('gulp-replace');


var path = {
    build: { //Укажем куда складывать готовые после сборки файлы
        html: 'build/htdocs',
        js: 'build/js/',
        css: 'build/css/',
        img: 'build/img/',
        fonts: 'build/fonts/'
    },
    src: { //Пути откуда брать исходники
        html: 'static/htdocs/*.html', //Синтаксис src/*.html говорит gulp что мы хотим взять все файлы с расширением .html
        js: 'static/js/main.js',//В стилях и скриптах нам понадобятся только main файлы
        style: 'static/css/main.scss',
        img: 'static/img/**/*.*', //Синтаксис img/**/*.* означает - взять все файлы всех расширений из папки и из вложенных каталогов
        fonts: 'static/fonts/**/*.*'
    },
    watch: { //Тут мы укажем, за изменением каких файлов мы хотим наблюдать
        html: 'static/htdocs/*.html',
        js: 'static/js/*.js',
        style: 'static/css/**/*.scss',
        img: 'static/img/**/*.*',
        fonts: 'static/fonts/**/*.*'
    },
    clean: './build'
};

var config = {
    server: {
        baseDir: "./build"
    },
    tunnel: true,
    host: 'localhost',
    port: 8000,
    logPrefix: "Frontend_Devil"
};

var packageJson = require('./package.json');

var cssToConcat = [
    './static/css/*.css'
];

var jsToConcat = [
    './static/js/*.js'
];

gulp.task('js', function() {
    return gulp.src(jsToConcat)
        .pipe(concatJs('bundle.js'))
        .pipe(gulp.dest('./static/js/'));
});

gulp.task('jsmin', ['js'], function() {
    return gulp.src('./static/js/bundle.js')
        .pipe(uglify())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./build/js/'));
});

gulp.task('concat-css', function() {
    return gulp.src(cssToConcat)
        .pipe(concatCss('bundle.css'))
        .pipe(gulp.dest('./static/css/'));
});

gulp.task('css', ['concat-css'], function () {
    return gulp.src('./static/css/bundle.css')
        .pipe(cssmin())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('./build/css/'));
});

gulp.task('images', function() {
    gulp.src('./static/img/**/*')
        .pipe(imagemin())
        .pipe(gulp.dest('./build/img'))

});

gulp.task('http-server', function() {
    connect()
        .use(require('connect-livereload')())
        .use(connect.static('./static'))
        .listen('8000');

    console.log('Server listening on http://localhost:9000');
});

gulp.task('watch', function() {
    // Предварительная сборка проекта
    // gulp.run('stylus');
    gulp.run('images');
    gulp.run('js');
    gulp.run('css');
    // Подключаем Livereload
    server.listen(35729, function(err) {
        if (err) return console.log(err);

        // gulp.watch('assets/stylus/**/*.styl', function() {
        //     gulp.run('stylus');
        // });

        gulp.watch('static/img/*', function() {
            gulp.run('images');
        });
        gulp.watch('static/js/*', function() {
            gulp.run('js');
        });
        gulp.watch('static/css/*', function() {
            gulp.run('css');
        });
    });
    gulp.run('http-server');
});

gulp.task('build', function() {
    // css
    gulp.src('./assets/stylus/screen.styl')
        .pipe(stylus({
            use: ['nib']
        })) // собираем stylus
    .pipe(myth()) // добавляем префиксы - http://www.myth.io/
    .pipe(csso()) // минимизируем css
    .pipe(gulp.dest('./build/css/')) // записываем css

    // js
    gulp.src(['./assets/js/**/*.js', '!./assets/js/vendor/**/*.js'])
        .pipe(concat('index.js'))
        .pipe(uglify())
        .pipe(gulp.dest('./build/js'));

    // image
    gulp.src('./assets/img/**/*')
        .pipe(imagemin())
        .pipe(gulp.dest('./build/img'))

});

gulp.task('build', ['jsmin', 'css']);
