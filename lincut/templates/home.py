from inui.elements import *

h = Html(
    lang="""fa""",
    dir="""rtl""",
    data=(
        Head(
            data=(
                Meta(
                    charset="""utf-8""",
                ),
                Meta(
                    http_equiv="""X-UA-Compatible""",
                    content="""IE=edge""",
                ),
                Meta(
                    name="""viewport""",
                    content="""width=device-width, initial-scale=1, shrink-to-fit=no""",
                ),
                Title(data=("""LinCut""",)),
                Meta(
                    name="""description""",
                    content="""LinCut is simple and fast link shortener that makes everything easy.""",
                ),
                Meta(
                    name="""keywords""",
                    content="""LinCut, Link, Link shortener, link cutter, url shortener""",
                ),
                Link(
                    rel="""icon""",
                    typee="""image/png""",
                    href="""https://bitn.ir/content/biiit.png""",
                    sizes="""32x32""",
                ),
                Link(
                    rel="""canonical""",
                    href="""https://bitn.ir""",
                ),
                Link(
                    rel="""stylesheet""",
                    href="""https://bitn.ir/static/frontend/libs/fontawesome/all.min.css""",
                ),
                Link(
                    rel="""stylesheet""",
                    typee="""text/css""",
                    href="""https://bitn.ir/static/frontend/libs/select2/dist/css/select2.min.css""",
                ),
                Link(
                    rel="""stylesheet""",
                    typee="""text/css""",
                    href="""https://bitn.ir/static/frontend/libs/cookieconsent/cookieconsent.css""",
                ),
                Link(
                    rel="""stylesheet""",
                    href="""https://bitn.ir/static/frontend/css/style.min.css""",
                    id="""stylesheet""",
                ),
                Link(
                    rel="""stylesheet""",
                    href="""https://bitn.ir/static/frontend/css/rtl.css""",
                    id="""stylesheet""",
                ),
                Link(
                    rel="""stylesheet""",
                    href="""https://bitn.ir/static/rtl/userpanel/mr-rtl.css""",
                    id="""stylesheet""",
                ),
                Script(
                    data=(
                        """
            var appurl = 'https://bitn.ir/';
        """,
                    )
                ),
            )
        ),
        Body(
            data=(
                Header(
                    classs="""header-transparent""",
                    id="""header-main""",
                    data=(
                        Nav(
                            classs="""navbar navbar-main navbar-expand-lg navbar-dark bg-dark""",
                            id="""navbar-main""",
                            data=(
                                Div(
                                    classs="""container border-0""",
                                    data=(
                                        A(
                                            classs="""navbar-brand""",
                                            href="""https://bitn.ir""",
                                            title="""کوتاه کننده لینک""",
                                            data=(
                                                Img(
                                                    alt="""کوتاه کننده لینک""",
                                                    src="""https://bitn.ir/content/logo-asli-sefed.png""",
                                                    id="""navbar-logo""",
                                                ),
                                            ),
                                        ),
                                        Button(
                                            classs="""navbar-toggler""",
                                            typee="""button""",
                                            data_toggle="""collapse""",
                                            data_target="""#navbar-main-collapse""",
                                            aria_controls="""navbar-main-collapse""",
                                            aria_expanded="""false""",
                                            aria_lable="""Toggle navigation""",
                                            data=(
                                                Span(
                                                    classs="""navbar-toggler-icon""",
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""collapse navbar-collapse navbar-collapse-overlay""",
                                            id="""navbar-main-collapse""",
                                            data=(
                                                Div(
                                                    classs="""position-relative""",
                                                    data=(
                                                        Button(
                                                            classs="""navbar-toggler""",
                                                            typee="""button""",
                                                            data_toggle="""collapse""",
                                                            data_target="""#navbar-main-collapse""",
                                                            aria_controls="""navbar-main-collapse""",
                                                            aria_expanded="""false""",
                                                            aria_lable="""Toggle navigation""",
                                                            data=(
                                                                I(
                                                                    data_feather="""x""",
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Ul(
                                                    classs="""navbar-nav ml-lg-auto""",
                                                    data=(
                                                        Li(
                                                            classs="""nav-item nav-item-spaced d-lg-block""",
                                                            data=(
                                                                A(
                                                                    classs="""nav-link""",
                                                                    href="""https://bitn.ir""",
                                                                    data=(
                                                                        """صفحه اصلی""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""nav-item nav-item-spaced d-lg-block""",
                                                            data=(
                                                                A(
                                                                    classs="""nav-link""",
                                                                    href="""https://bitn.ir/pricing""",
                                                                    data=(
                                                                        """قیمت گذاری""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""nav-item nav-item-spaced dropdown dropdown-animate""",
                                                            data_toggle="""hover""",
                                                            data=(
                                                                A(
                                                                    classs="""nav-link""",
                                                                    data_toggle="""dropdown""",
                                                                    href="""#""",
                                                                    aria_haspopup="""true""",
                                                                    aria_expanded="""false""",
                                                                    data=(
                                                                        """راه حل ها""",
                                                                    ),
                                                                ),
                                                                Div(
                                                                    classs="""dropdown-menu dropdown-menu-xl p-0""",
                                                                    data=(
                                                                        Div(
                                                                            classs="""row no-gutters""",
                                                                            data=(
                                                                                Div(
                                                                                    classs="""col-12 col-lg-6 order-lg-2""",
                                                                                    data=(
                                                                                        Div(
                                                                                            classs="""dropdown-body dropdown-body-right bg-dropdown-secondary h-100""",
                                                                                            data=(
                                                                                                H6(
                                                                                                    classs="""dropdown-header""",
                                                                                                    data=(
                                                                                                        """
                            منابع                        """,
                                                                                                    ),
                                                                                                ),
                                                                                                Div(
                                                                                                    classs="""list-group list-group-flush""",
                                                                                                    data=(
                                                                                                        Div(
                                                                                                            classs="""list-group-item bg-transparent border-0 px-0 py-2""",
                                                                                                            data=(
                                                                                                                Div(
                                                                                                                    classs="""media d-flex""",
                                                                                                                    data=(
                                                                                                                        Span(
                                                                                                                            classs="""h6""",
                                                                                                                            data=(
                                                                                                                                I(
                                                                                                                                    data_feather="""code""",
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        Div(
                                                                                                                            classs="""media-body ml-2""",
                                                                                                                            data=(
                                                                                                                                A(
                                                                                                                                    href="""https://bitn.ir/developers""",
                                                                                                                                    classs="""d-block h6 mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """API""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                                Small(
                                                                                                                                    classs="""text-sm text-muted mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """راهنمای نحوه استفاده از API ما""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                ),
                                                                                                            ),
                                                                                                        ),
                                                                                                    ),
                                                                                                ),
                                                                                                Div(
                                                                                                    classs="""list-group list-group-flush""",
                                                                                                    data=(
                                                                                                        Div(
                                                                                                            classs="""list-group-item bg-transparent border-0 px-0 py-2""",
                                                                                                            data=(
                                                                                                                Div(
                                                                                                                    classs="""media d-flex""",
                                                                                                                    data=(
                                                                                                                        Span(
                                                                                                                            classs="""h6""",
                                                                                                                            data=(
                                                                                                                                I(
                                                                                                                                    data_feather="""help-circle""",
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        Div(
                                                                                                                            classs="""media-body ml-2""",
                                                                                                                            data=(
                                                                                                                                A(
                                                                                                                                    href="""https://bitn.ir/help""",
                                                                                                                                    classs="""d-block h6 mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """مرکز کمک""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                                Small(
                                                                                                                                    classs="""text-sm text-muted mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """مرکز راهنمایی ما را بررسی کنید""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                ),
                                                                                                            ),
                                                                                                        ),
                                                                                                    ),
                                                                                                ),
                                                                                            ),
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                                Div(
                                                                                    classs="""col-12 col-lg-6 order-lg-1 mt-4 mt-lg-0""",
                                                                                    data=(
                                                                                        Div(
                                                                                            classs="""dropdown-body""",
                                                                                            data=(
                                                                                                H6(
                                                                                                    classs="""dropdown-header""",
                                                                                                    data=(
                                                                                                        """
                            راه حل ها                        """,
                                                                                                    ),
                                                                                                ),
                                                                                                Div(
                                                                                                    classs="""list-group list-group-flush""",
                                                                                                    data=(
                                                                                                        Div(
                                                                                                            classs="""list-group-item border-0""",
                                                                                                            data=(
                                                                                                                Div(
                                                                                                                    classs="""media d-flex""",
                                                                                                                    data=(
                                                                                                                        Div(
                                                                                                                            classs="""media-body""",
                                                                                                                            data=(
                                                                                                                                A(
                                                                                                                                    href="""https://bitn.ir/qr-codes""",
                                                                                                                                    classs="""d-block h6 mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """ساخت بارکد QR حرفه ای""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                                Small(
                                                                                                                                    classs="""text-sm text-muted mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """کدهای QR قابل تنظیم و ردیابی""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                ),
                                                                                                            ),
                                                                                                        ),
                                                                                                        Div(
                                                                                                            classs="""list-group-item border-0""",
                                                                                                            data=(
                                                                                                                Div(
                                                                                                                    classs="""media d-flex""",
                                                                                                                    data=(
                                                                                                                        Div(
                                                                                                                            classs="""media-body""",
                                                                                                                            data=(
                                                                                                                                A(
                                                                                                                                    href="""https://bitn.ir/bio-profiles""",
                                                                                                                                    classs="""d-block h6 mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """صفحات بیو""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                                Small(
                                                                                                                                    classs="""text-sm text-muted mb-0""",
                                                                                                                                    data=(
                                                                                                                                        """فالوورهای شبکه های اجتماعی خود را تبدیل کنید""",
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                ),
                                                                                                            ),
                                                                                                        ),
                                                                                                    ),
                                                                                                ),
                                                                                            ),
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""nav-item nav-item-spaced d-lg-block""",
                                                            data=(
                                                                A(
                                                                    classs="""nav-link""",
                                                                    href="""https://bitn.ir/blog""",
                                                                    data=("""وبلاگ""",),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Ul(
                                                    classs="""navbar-nav align-items-lg-center d-none d-lg-flex ml-lg-auto""",
                                                    data=(
                                                        Li(
                                                            classs="""nav-item""",
                                                            data=(
                                                                A(
                                                                    classs="""nav-link""",
                                                                    href="""https://bitn.ir/user/login""",
                                                                    data=(
                                                                        """وارد شوید""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        Li(
                                                            classs="""nav-item""",
                                                            data=(
                                                                A(
                                                                    href="""https://bitn.ir/user/register""",
                                                                    classs="""btn btn-sm btn-success btn-icon ml-3""",
                                                                    data=(
                                                                        Span(
                                                                            classs="""btn-inner--text""",
                                                                            data=(
                                                                                """ثبت نام رایگان""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""d-lg-none px-4 text-center""",
                                                    data=(
                                                        Div(
                                                            classs="""d-flex""",
                                                            data=(
                                                                Div(
                                                                    classs="""w-50 mr-1""",
                                                                    data=(
                                                                        A(
                                                                            href="""https://bitn.ir/user/login""",
                                                                            classs="""btn btn-block btn-sm btn-primary""",
                                                                            data=(
                                                                                """وارد شوید""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                Div(
                                                                    classs="""w-50 ml-1""",
                                                                    data=(
                                                                        A(
                                                                            href="""https://bitn.ir/user/register""",
                                                                            classs="""btn btn-block btn-sm btn-primary""",
                                                                            data=(
                                                                                """ثبت نام رایگان""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                Section(
                    classs="""slice pt-md-8 pb-5 pt-5 bg-section-dark""",
                    style="""background: linear-gradient(220.55deg, #3b7ddd 0%, #3b7ddd 100%) !important;""",
                    data=(
                        Div(
                            classs="""my-5""",
                            data_offset_top="""#navbar-main""",
                            data=(
                                Div(
                                    classs="""container position-relative""",
                                    data=(
                                        Div(
                                            classs="""row align-items-center""",
                                            data=(
                                                Div(
                                                    classs="""col-12 col-lg-6 pr-lg-5""",
                                                    data=(
                                                        H1(
                                                            classs="""display-3 text-white font-weight-bolder mb-4""",
                                                            data=(
                                                                """
                        کوتاه کننده لینک                    """,
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""lead text-white opacity-8""",
                                                            data=(
                                                                """
                        بیتن | کوتاه کننده لینک با پایداری بالا مناسب کمپین های تبلیغاتی با کنترل پنل حرفه ای و آمار دقیق + ابزار های ویژه QR کد ساز و ایجاد کننده صفحات بیو و دیگر امکانات حرفه ای                    """,
                                                            ),
                                                        ),
                                                        Form(
                                                            classs="""mt-5""",
                                                            method="""post""",
                                                            action="""https://bitn.ir/shorten""",
                                                            data_trigger="""shorten-form""",
                                                            data=(
                                                                Div(
                                                                    classs="""input-group input-group-lg mb-3""",
                                                                    data=(
                                                                        Input(
                                                                            typee="""text""",
                                                                            classs="""form-control""",
                                                                            placeholder="""لینک اصلی را اینجا وارد کنید""",
                                                                            name="""url""",
                                                                            id="""url""",
                                                                        ),
                                                                        Div(
                                                                            classs="""input-group-append""",
                                                                            data=(
                                                                                Button(
                                                                                    classs="""btn btn-warning d-none""",
                                                                                    typee="""button""",
                                                                                    data=(
                                                                                        """کپی""",
                                                                                    ),
                                                                                ),
                                                                                Button(
                                                                                    classs="""btn btn-success""",
                                                                                    typee="""submit""",
                                                                                    data=(
                                                                                        """کوتاه کن""",
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                Div(
                                                                    classs="""g-recaptcha mb-3""",
                                                                    data_sitekey="""6LdVjngaAAAAACRpxMq3lUMLj1UhQxeIC4oGPaYF""",
                                                                    data_action="""shorten""",
                                                                ),
                                                                Script(
                                                                    src="""https://www.google.com/recaptcha/api.js?hl=fa""",
                                                                    asyncc="",
                                                                    defer="""defer""",
                                                                ),
                                                                Script(
                                                                    data=(
                                                                        """
                    var recaptcha = () => {
                        return grecaptcha.reset();
                    }
                """,
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            id="""output-result""",
                                                            classs="""border border-success p-3 rounded d-none""",
                                                            data=(
                                                                Div(
                                                                    classs="""row""",
                                                                    data=(
                                                                        Div(
                                                                            id="""qr-result""",
                                                                            classs="""col-md-4 p-2""",
                                                                        ),
                                                                        Div(
                                                                            id="""text-result""",
                                                                            classs="""col-md-8""",
                                                                            data=(
                                                                                P(
                                                                                    classs="""text-white""",
                                                                                    data=(
                                                                                        """لینک شما با موفقیت کوتاه شد. آیا می خواهید تنظیمات و گزینه های سفارشی سازی بیشتری داشته باشید؟""",
                                                                                    ),
                                                                                ),
                                                                                A(
                                                                                    href="""https://bitn.ir/user/register""",
                                                                                    classs="""btn btn-sm btn-primary""",
                                                                                    data=(
                                                                                        """شروع کنید""",
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""col-12 col-lg-6 mt-7 mt-lg-0""",
                                                    data=(
                                                        Div(
                                                            classs="""position-relative left-8 left-lg-0 d-none d-lg-block""",
                                                            data=(
                                                                Figure(
                                                                    data=(
                                                                        Img(
                                                                            src="""https://bitn.ir/content/zBSzih_hero_کوتاه کننده لینک 1.png""",
                                                                            alt="""کوتاه کننده لینک""",
                                                                            classs="""img-fluid mw-lg-120 rounded-top zindex-100""",
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                Footer(
                    classs="""position-relative""",
                    id="""footer-main""",
                    data=(
                        Div(
                            classs="""footer pt-lg-7 footer-dark bg-section-dark""",
                            data=(
                                Div(
                                    classs="""container pt-4""",
                                    data=(
                                        Div(
                                            classs="""row justify-content-center""",
                                            data=(
                                                Div(
                                                    classs="""col-lg-12""",
                                                    data=(
                                                        Div(
                                                            classs="""row align-items-center""",
                                                            data=(
                                                                Div(
                                                                    classs="""col-lg-7""",
                                                                    data=(
                                                                        H3(
                                                                            classs="""text-secondary mb-2""",
                                                                            data=(
                                                                                """بازاریابی با اطمینان""",
                                                                            ),
                                                                        ),
                                                                        P(
                                                                            classs="""lead mb-0 text-white opacity-8""",
                                                                            data=(
                                                                                """
                                کمپین بازاریابی خود را هم اکنون شروع کنید و به طور موثر به مشتریان خود دسترسی پیدا کنید.                            """,
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                Div(
                                                                    classs="""col-lg-5 text-lg-right mt-4 mt-lg-0""",
                                                                    data=(
                                                                        A(
                                                                            href="""https://bitn.ir/user/register""",
                                                                            classs="""btn btn-primary my-2 ml-0 ml-sm-3""",
                                                                            data=(
                                                                                """
                                ثبت نام رایگان                            """,
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Hr(
                                            classs="""divider divider-fade divider-dark my-5""",
                                        ),
                                        Div(
                                            classs="""row""",
                                            data=(
                                                Div(
                                                    classs="""col-lg-4 mb-5 mb-lg-0""",
                                                    data=(
                                                        P(
                                                            classs="""mt-4 text-sm opacity-8 pr-lg-4""",
                                                            data=(
                                                                """بیتن | کوتاه کننده لینک با پایداری بالا مناسب کمپین های تبلیغاتی با کنترل پنل حرفه ای و آمار دقیق + ابزار های ویژه QR کد ساز و ایجاد کننده صفحات بیو و دیگر امکانات حرفه ای""",
                                                            ),
                                                        ),
                                                        Ul(
                                                            classs="""nav mt-4""",
                                                            data=(),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""col-lg-4 col-6 col-sm-6 ml-lg-auto mb-5 mb-lg-0""",
                                                    data=(
                                                        H6(
                                                            classs="""heading mb-3""",
                                                            data=("""راه حل ها""",),
                                                        ),
                                                        Ul(
                                                            classs="""list-unstyled""",
                                                            data=(
                                                                Li(
                                                                    data=(
                                                                        A(
                                                                            href="""https://bitn.ir/qr-codes""",
                                                                            data=(
                                                                                """ساخت بارکد QR حرفه ای""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                                Li(
                                                                    data=(
                                                                        A(
                                                                            href="""https://bitn.ir/bio-profiles""",
                                                                            data=(
                                                                                """بیو پروفایل""",
                                                                            ),
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""col-lg-4 col-6 col-sm-6 mb-5 mb-lg-0""",
                                                    data=(
                                                        H6(
                                                            classs="""heading mb-3""",
                                                            data=("""شرکت""",),
                                                        ),
                                                        Ul(
                                                            classs="""list-unstyled""",
                                                            data=(
                                                                Li(
                                                                    classs="""nav-item""",
                                                                    data=(
                                                                        A(
                                                                            classs="""nav-link""",
                                                                            href="""https://bitn.ir/help""",
                                                                            data=(
                                                                                """مرکز کمک""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                Li(
                                                                    classs="""nav-item""",
                                                                    data=(
                                                                        A(
                                                                            classs="""nav-link""",
                                                                            href="""https://bitn.ir/developers""",
                                                                            data=(
                                                                                """API""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                Li(
                                                                    classs="""nav-item""",
                                                                    data=(
                                                                        A(
                                                                            classs="""nav-link""",
                                                                            href="""https://bitn.ir/contact""",
                                                                            data=(
                                                                                """تماس با ما""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Hr(
                                            classs="""divider divider-fade divider-dark my-4""",
                                        ),
                                        Div(
                                            classs="""row align-items-center justify-content-md-between pb-4""",
                                            data=(
                                                Div(
                                                    classs="""col-md-4""",
                                                    data=(
                                                        Div(
                                                            classs="""copyright text-sm font-weight-bold text-center text-md-left""",
                                                            data=(
                                                                """
                        © ۱۴۰۲ """,
                                                                A(
                                                                    href="""https://bitn.ir""",
                                                                    classs="""font-weight-bold""",
                                                                    data=(
                                                                        """کوتاه کننده لینک""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""col-md-8""",
                                                    data=(
                                                        Ul(
                                                            classs="""nav justify-content-center justify-content-md-end mt-3 mt-md-0""",
                                                            data=(
                                                                Li(
                                                                    classs="""nav-item""",
                                                                    data=(
                                                                        A(
                                                                            classs="""nav-link""",
                                                                            href="""https://bitn.ir/page/gavanin""",
                                                                            data=(
                                                                                """قوانین و شرایط""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                Li(
                                                                    classs="""nav-item""",
                                                                    data=(
                                                                        A(
                                                                            classs="""nav-link""",
                                                                            href="""https://bitn.ir/report""",
                                                                            data=(
                                                                                """گزارش""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                Li(
                                                                    classs="""nav-item dropup""",
                                                                    data=(
                                                                        A(
                                                                            classs="""nav-link""",
                                                                            data_toggle="""dropdown""",
                                                                            href="""#""",
                                                                            data=(
                                                                                I(
                                                                                    data_feather="""globe""",
                                                                                    classs="""mr-1""",
                                                                                ),
                                                                            ),
                                                                        ),
                                                                        Ul(
                                                                            classs="""dropdown-menu""",
                                                                            data=(
                                                                                Li(
                                                                                    data=(
                                                                                        A(
                                                                                            classs="""dropdown-item""",
                                                                                            href="""?lang=fa""",
                                                                                            data=(
                                                                                                """Persian""",
                                                                                            ),
                                                                                        ),
                                                                                    )
                                                                                ),
                                                                                Li(
                                                                                    data=(
                                                                                        A(
                                                                                            classs="""dropdown-item""",
                                                                                            href="""?lang=en""",
                                                                                            data=(
                                                                                                """English""",
                                                                                            ),
                                                                                        ),
                                                                                    )
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                Script(
                    src="""https://bitn.ir/static/bundle.pack.js""",
                ),
                Script(
                    src="""https://bitn.ir/static/frontend/libs/clipboard/dist/clipboard.min.js""",
                ),
                Script(
                    typee="""text/javascript""",
                    data=(
                        """
            var lang = {"error":"\u0644\u0637\u0641\u0627 \u06cc\u06a9 \u0646\u0634\u0627\u0646\u06cc \u0648\u0628 \u0645\u0639\u062a\u0628\u0631 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f.","couponinvalid":"\u06a9\u0648\u067e\u0646 \u0648\u0627\u0631\u062f \u0634\u062f\u0647 \u0645\u0639\u062a\u0628\u0631 \u0646\u06cc\u0633\u062a","minurl":"\u0634\u0645\u0627 \u0628\u0627\u06cc\u062f \u062d\u062f\u0627\u0642\u0644 1 \u0622\u062f\u0631\u0633 \u0627\u06cc\u0646\u062a\u0631\u0646\u062a\u06cc \u0631\u0627 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f.","minsearch":"\u06a9\u0644\u0645\u0647 \u06a9\u0644\u06cc\u062f\u06cc \u0628\u0627\u06cc\u062f \u0628\u06cc\u0634 \u0627\u0632 3 \u06a9\u0627\u0631\u0627\u06a9\u062a\u0631 \u0628\u0627\u0634\u062f!","nodata":"\u0647\u06cc\u0686 \u062f\u0627\u062f\u0647 \u0627\u06cc \u0628\u0631\u0627\u06cc \u0627\u06cc\u0646 \u062f\u0631\u062e\u0648\u0627\u0633\u062a \u062f\u0631 \u062f\u0633\u062a\u0631\u0633 \u0646\u06cc\u0633\u062a.","datepicker":{"7d":"Last 7 Days","3d":"Last 30 Days","tm":"This Month","lm":"Last Month"},"cookie":{"title":"\u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u06a9\u0648\u06a9\u06cc","description":"\u0627\u06cc\u0646 \u0648\u0628 \u0633\u0627\u06cc\u062a \u0627\u0632 \u06a9\u0648\u06a9\u06cc \u0647\u0627\u06cc \u0636\u0631\u0648\u0631\u06cc \u0628\u0631\u0627\u06cc \u0627\u0637\u0645\u06cc\u0646\u0627\u0646 \u0627\u0632 \u0639\u0645\u0644\u06a9\u0631\u062f \u0635\u062d\u06cc\u062d \u0648 \u067e\u06cc\u06af\u06cc\u0631\u06cc \u06a9\u0648\u06a9\u06cc \u0647\u0627 \u0628\u0631\u0627\u06cc \u062f\u0631\u06a9 \u0646\u062d\u0648\u0647 \u062a\u0639\u0627\u0645\u0644 \u0634\u0645\u0627 \u0628\u0627 \u0622\u0646 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0645\u06cc \u06a9\u0646\u062f. \u0634\u0645\u0627 \u0627\u06cc\u0646 \u0627\u0645\u06a9\u0627\u0646 \u0631\u0627 \u062f\u0627\u0631\u06cc\u062f \u06a9\u0647 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f \u06a9\u062f\u0627\u0645 \u06cc\u06a9 \u0631\u0627 \u0645\u062c\u0627\u0632 \u06a9\u0646\u06cc\u062f.","button":" <button type=\"button\" data-cc=\"c-settings\" class=\"cc-link\" aria-haspopup=\"dialog\">\u0628\u06af\u0630\u0627\u0631 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u0645<\/button>","accept_all":"\u067e\u0630\u06cc\u0631\u0634 \u0647\u0645\u0647 \u0645\u0648\u0627\u0631\u062f","accept_necessary":"\u0644\u0627\u0632\u0645 \u0631\u0627 \u0628\u067e\u0630\u06cc\u0631\u06cc\u062f","close":"\u0628\u0633\u062a\u0646","save":"\u0630\u062e\u06cc\u0631\u0647 \u062a\u0646\u0638\u06cc\u0645\u0627\u062a","necessary":{"title":"\u06a9\u0648\u06a9\u06cc \u0647\u0627\u06cc \u06a9\u0627\u0645\u0644\u0627 \u0636\u0631\u0648\u0631\u06cc","description":"\u0627\u06cc\u0646 \u06a9\u0648\u06a9\u06cc \u0647\u0627 \u0628\u0631\u0627\u06cc \u0639\u0645\u0644\u06a9\u0631\u062f \u0635\u062d\u06cc\u062d \u0633\u0631\u0648\u06cc\u0633 \u0645\u0627 \u0645\u0648\u0631\u062f \u0646\u06cc\u0627\u0632 \u0647\u0633\u062a\u0646\u062f \u0648 \u0628\u062f\u0648\u0646 \u0627\u06cc\u0646 \u06a9\u0648\u06a9\u06cc \u0647\u0627 \u0646\u0645\u06cc \u062a\u0648\u0627\u0646\u06cc\u062f \u0627\u0632 \u0645\u062d\u0635\u0648\u0644 \u0645\u0627 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u06a9\u0646\u06cc\u062f."},"analytics":{"title":"\u0647\u062f\u0641 \u06af\u0630\u0627\u0631\u06cc \u0648 \u062a\u062c\u0632\u06cc\u0647 \u0648 \u062a\u062d\u0644\u06cc\u0644","description":"\u0627\u0631\u0627\u0626\u0647\u200c\u062f\u0647\u0646\u062f\u06af\u0627\u0646\u06cc \u0645\u0627\u0646\u0646\u062f Google \u0627\u0632 \u0627\u06cc\u0646 \u06a9\u0648\u06a9\u06cc\u200c\u0647\u0627 \u0628\u0631\u0627\u06cc \u0627\u0646\u062f\u0627\u0632\u0647\u200c\u06af\u06cc\u0631\u06cc \u0648 \u0627\u0631\u0627\u0626\u0647 \u062a\u062d\u0644\u06cc\u0644\u200c\u0647\u0627\u06cc\u06cc \u062f\u0631 \u0645\u0648\u0631\u062f \u0646\u062d\u0648\u0647 \u062a\u0639\u0627\u0645\u0644 \u0634\u0645\u0627 \u0628\u0627 \u0648\u0628\u200c\u0633\u0627\u06cc\u062a \u0645\u0627 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0645\u06cc\u200c\u06a9\u0646\u0646\u062f. \u0647\u0645\u0647 \u062f\u0627\u062f\u0647 \u0647\u0627 \u0646\u0627\u0634\u0646\u0627\u0633 \u0647\u0633\u062a\u0646\u062f \u0648 \u0646\u0645\u06cc \u062a\u0648\u0627\u0646 \u0627\u0632 \u0622\u0646\u0647\u0627 \u0628\u0631\u0627\u06cc \u0634\u0646\u0627\u0633\u0627\u06cc\u06cc \u0634\u0645\u0627 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u06a9\u0631\u062f."},"ads":{"title":"\u062a\u0628\u0644\u06cc\u063a\u0627\u062a","description":"\u0627\u06cc\u0646 \u06a9\u0648\u06a9\u06cc\u200c\u0647\u0627 \u062a\u0648\u0633\u0637 \u062a\u0628\u0644\u06cc\u063a\u200c\u06a9\u0646\u0646\u062f\u06af\u0627\u0646 \u0645\u0627 \u062a\u0646\u0638\u06cc\u0645 \u0634\u062f\u0647\u200c\u0627\u0646\u062f \u062a\u0627 \u0628\u062a\u0648\u0627\u0646\u0646\u062f \u062a\u0628\u0644\u06cc\u063a\u0627\u062a \u0645\u0631\u062a\u0628\u0637 \u0631\u0627 \u062f\u0631 \u0627\u062e\u062a\u06cc\u0627\u0631 \u0634\u0645\u0627 \u0642\u0631\u0627\u0631 \u062f\u0647\u0646\u062f."},"extra":{"title":"\u0639\u0645\u0644\u06a9\u0631\u062f \u0627\u0636\u0627\u0641\u06cc","description":"\u0645\u0627 \u0627\u0632 \u0627\u0631\u0627\u0626\u0647 \u062f\u0647\u0646\u062f\u06af\u0627\u0646 \u0645\u062e\u062a\u0644\u0641\u06cc \u0628\u0631\u0627\u06cc \u0628\u0647\u0628\u0648\u062f \u0645\u062d\u0635\u0648\u0644\u0627\u062a \u062e\u0648\u062f \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0645\u06cc \u06a9\u0646\u06cc\u0645 \u0648 \u0622\u0646\u0647\u0627 \u0645\u0645\u06a9\u0646 \u0627\u0633\u062a \u06a9\u0648\u06a9\u06cc \u0647\u0627 \u0631\u0627 \u062a\u0646\u0638\u06cc\u0645 \u06a9\u0646\u0646\u062f \u06cc\u0627 \u0646\u06a9\u0646\u0646\u062f. \u0628\u0647\u0628\u0648\u062f \u0645\u06cc \u062a\u0648\u0627\u0646\u062f \u0634\u0627\u0645\u0644 \u0634\u0628\u06a9\u0647 \u0647\u0627\u06cc \u062a\u062d\u0648\u06cc\u0644 \u0645\u062d\u062a\u0648\u0627\u060c \u0641\u0648\u0646\u062a \u0647\u0627\u06cc \u06af\u0648\u06af\u0644 \u0648 \u063a\u06cc\u0631\u0647 \u0628\u0627\u0634\u062f"},"privacy":{"title":"\u0633\u06cc\u0627\u0633\u062a \u062d\u0641\u0638 \u062d\u0631\u06cc\u0645 \u062e\u0635\u0648\u0635\u06cc","description":"\u0634\u0645\u0627 \u0645\u06cc \u062a\u0648\u0627\u0646\u06cc\u062f \u0633\u06cc\u0627\u0633\u062a \u062d\u0641\u0638 \u062d\u0631\u06cc\u0645 \u062e\u0635\u0648\u0635\u06cc \u0645\u0627 \u0631\u0627 \u0628\u0628\u06cc\u0646\u06cc\u062f <a target=\"_blank\" class=\"cc-link\" href=\"https:\/\/bitn.ir\/page\/privacy\">\u0627\u06cc\u0646\u062c\u0627<\/a>. \u0627\u06af\u0631 \u0633\u0648\u0627\u0644\u06cc \u062f\u0627\u0631\u06cc\u062f\u060c \u0644\u0637\u0641\u0627 \u062f\u0631\u06cc\u063a \u0646\u06a9\u0646\u06cc\u062f <a href=\"https:\/\/bitn.ir\/contact\" target=\"_blank\" class=\"cc-link\">\u062a\u0645\u0627\u0633 \u0628\u0627 \u0645\u0627<\/a>"}}}        """,
                    ),
                ),
                Script(
                    data=(
                        """
            feather.replace({
                'width': '1em',
                'height': '1em'
            })
        """,
                    )
                ),
                Script(
                    src="""https://bitn.ir/static/frontend/js/app.min.js?v=1.2""",
                ),
                Script(
                    src="""https://bitn.ir/static/server.min.js?v=1.2""",
                ),
                Script(
                    typee="""text/javascript""",
                    data=(
                        """
  !function(){var i="KbqREr",a=window,d=document;function g(){var g=d.createElement("script"),s="https://www.goftino.com/widget/"+i,l=localStorage.getItem("goftino_"+i);g.async=!0,g.src=l?s+"?o="+l:s;d.getElementsByTagName("head")[0].appendChild(g);}"complete"===d.readyState?g():a.attachEvent?a.attachEvent("onload",g):a.addEventListener("load",g,!1);}();
""",
                    ),
                ),
            )
        ),
    ),
)

h.save("index.html")
