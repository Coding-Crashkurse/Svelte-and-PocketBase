<script>
    import '../app.css';
    let year = new Date().getFullYear();
</script>

<div class="nav-wrapper bg-black p-2 text-white absolute w-full">
    <div class="max-w-screen-xl flex justify-between mx-auto flex-col md:flex-row">
        <div class="flex items-center justify-center">
            <div class="btn btn-ghost normal-case text-xl">Coding Crash Courses</div>
        </div>

        <div class="flex justify-center">
            <a href="/" class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl">
                Home
                <span class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600" />
            </a>
            <a href="/courses" class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl">
                Courses
                <span class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600" />
            </a>
            <a href="/premium" class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl">
                Premium
                <span class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600" />
            </a>
            <a href="/about" class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl">
                About
                <span class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600" />
            </a>
            <a href="/contact" class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl">
                Contact
                <span class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600" />
            </a>
        </div>
    </div>
</div>

<slot />

<footer>
    <div class="footer bg-black h-10 text-white flex items-center">
        <div class="inline text-center w-full">
            Copyright {year} Coding Crash Courses, All rights reserved | <a href="/impressum">Impressum</a> |
            <a href="/datenschutzerklaerung">Privacy Policy</a>
        </div>
    </div>
</footer>
