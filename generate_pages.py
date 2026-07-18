import os

FILE_TOP = "index.html"
FILE_ARCHIVE = "archive.html"
FILE_PROFILE = "profile.html"
FILE_CONTACT = "contact.html"

def get_header(active_page):
    # AOS Integration: load on all pages except contact
    aos_css = ""
    if active_page != "contact":
        aos_css = '<link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />'
        
    nav_html = ""
    if active_page == "top":
        nav_html = f"""    <nav x-data="{{ scrolled: false }}"
         @scroll.window="scrolled = (window.pageYOffset > 50)"
         :class="scrolled ? 'bg-[#002D5B]/95 shadow-md backdrop-blur-md border-transparent' : 'bg-transparent shadow-none border-b border-white/10'"
         class="text-white fixed top-0 left-0 w-full z-50 transition-all duration-300 border-b">"""
    else:
        nav_html = f"""    <nav class="bg-[#002D5B] text-white sticky top-0 z-50 shadow-md backdrop-blur-md bg-opacity-95">"""

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Favicon -->
    <link rel="icon" href="../images/favicon.ico" type="image/x-icon">
    <link rel="icon" href="../images/favicon.png" type="image/png" sizes="32x32">
    <link rel="apple-touch-icon" href="../images/favicon-192.png" sizes="192x192">
    <title>LOGISTICS FRONTIER INTERVIEWS | 日本物流の「知」と「経験」を次代へ継承する</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link class="font-awesome" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    {aos_css}
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Poppins:wght@600;700&display=swap');
        body {{ font-family: 'Noto Sans JP', sans-serif; }}
        .font-poppins {{ font-family: 'Poppins', sans-serif; }}
        :root {{
            --waseda-navy: #002D5B;
            --accent-red: #9E1B32;
        }}
        .bg-grid-pattern {{
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(0, 45, 91, 0.015) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(0, 45, 91, 0.015) 1px, transparent 1px);
        }}
        .text-shadow {{ text-shadow: 0 2px 8px rgba(0,0,0,0.7); }}
        html {{
            scroll-behavior: smooth;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 bg-grid-pattern relative min-h-screen">

    <!-- Ambient glowing backgrounds -->
    <div class="absolute top-1/4 left-0 w-96 h-96 bg-[#002D5B]/3 rounded-full blur-3xl pointer-events-none hidden md:block"></div>
    <div class="absolute top-1/2 right-0 w-96 h-96 bg-[#9E1B32]/3 rounded-full blur-3xl pointer-events-none hidden md:block"></div>

    {nav_html}
        <div class="w-full px-4 sm:px-6 lg:px-12 py-4 flex flex-col md:flex-row justify-between items-center gap-4">
            <div class="flex flex-col md:flex-row items-center md:space-x-3 text-center md:text-left">
                <a href="{FILE_TOP}" class="flex items-center space-x-2.5 font-poppins text-lg sm:text-xl md:text-2xl font-bold tracking-wider">
                    <img src="../images/logo_icon.png" alt="LOGISTICS FRONTIER INTERVIEWS" class="h-8 w-auto">
                    <span class="flex flex-wrap items-center justify-center md:justify-start gap-x-2">
                        <span class="inline-block whitespace-nowrap">LOGISTICS FRONTIER</span>
                        <span class="text-[#D12442] inline-block whitespace-nowrap">INTERVIEWS</span>
                    </span>
                </a>
            </div>
            <div class="flex space-x-3 sm:space-x-6 text-xs sm:text-sm md:text-base font-medium md:mr-12 lg:mr-24 xl:mr-32">
                <a href="{FILE_TOP}" class="pb-1 border-b-2 transition-all { 'text-white border-[#9E1B32] font-bold' if active_page == 'top' else 'border-transparent hover:text-slate-300' }">TOP</a>
                <a href="{FILE_ARCHIVE}" class="pb-1 border-b-2 transition-all { 'text-white border-[#9E1B32] font-bold' if active_page == 'archive' else 'border-transparent hover:text-slate-300' }">取材記事</a>
                <a href="{FILE_PROFILE}" class="pb-1 border-b-2 transition-all { 'text-white border-[#9E1B32] font-bold' if active_page == 'profile' else 'border-transparent hover:text-slate-300' }">運営・研究室</a>
                <a href="{FILE_CONTACT}" class="pb-1 border-b-2 transition-all { 'text-white border-[#9E1B32] font-bold' if active_page == 'contact' else 'border-transparent hover:text-slate-300' }">お問い合わせ</a>
            </div>
        </div>
    </nav>
"""

def get_footer(active_page):
    # AOS Integration: init on all pages except contact
    aos_js = ""
    if active_page != "contact":
        aos_js = """
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 800,
            once: true,
            offset: 80,
            easing: 'ease-out-cubic'
        });
    </script>
"""
    return f"""
    <footer class="bg-slate-900 text-slate-400 text-[11px] py-6 border-t border-slate-800 mt-12 relative z-10">
        <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-2">
            <div class="text-center md:text-left">
                <p class="font-poppins font-bold text-slate-300 text-xs tracking-wider">LOGISTICS FRONTIER INTERVIEWS</p>
                <p class="mt-0.5 text-slate-500">Logistics Knowledge & Network Hub</p>
            </div>
            <div class="text-slate-500">
                <p>&copy; 2026 LOGISTICS FRONTIER INTERVIEWS Project. All rights reserved.</p>
            </div>
        </div>
    </footer>
    {aos_js}
</body>
</html>
"""

top_content = f"""
    <!-- ① ディスプレイの高さに完全自動調整する全画面ヒーローセクション -->
    <div class="relative w-full h-screen min-h-[520px] flex items-center justify-center bg-slate-950 overflow-hidden" data-aos="fade-in">
        
        <!-- ② 背景動画を埋め込むための箱（videoタグ） -->
        <video autoplay muted loop playsinline class="absolute inset-0 w-full h-full object-cover opacity-35">
            <source src="../videos/truckship.mp4" type="video/mp4">
            <!-- 代替用背景画像 -->
            <img src="../images/image_c890cb.jpg" alt="Logistics Truck" class="w-full h-full object-cover">
        </video>
        
        <!-- 紺色グラデーションマスク -->
        <div class="absolute inset-0 bg-gradient-to-b from-[#002D5B]/70 via-[#002D5B]/40 to-[#002D5B]/70"></div>
        
        <div class="relative z-10 max-w-7xl mx-auto px-6 text-center text-shadow flex flex-col items-center justify-center h-full text-white">
            <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-poppins font-bold leading-tight mb-4 tracking-wider w-full mx-auto">
                <span class="flex flex-wrap justify-center gap-x-4">
                    <span class="inline-block whitespace-nowrap">LOGISTICS FRONTIER</span>
                    <span class="text-[#D12442] drop-shadow-[0_0_15px_rgba(209,36,66,0.4)] inline-block whitespace-nowrap">INTERVIEWS</span>
                </span>
            </h1>
            <p class="text-lg sm:text-xl md:text-2xl lg:text-3xl font-bold mb-8 tracking-tight w-full mx-auto text-slate-100">
                <span class="inline-block">日本物流の</span><span class="inline-block">「知」と「経験」を</span><span class="inline-block">次代へ継承する</span>
            </p>
            <p class="text-xs sm:text-sm md:text-base text-slate-200 leading-relaxed mb-10 max-w-4xl mx-auto px-4">
                <span class="inline-block">物流・サプライチェーン of 最前線で</span><span class="inline-block">挑戦し続ける方々の</span><span class="inline-block">意思決定や経験をインタビューし、</span><span class="inline-block">その知見を記録・発信するプロジェクト。</span><br class="hidden lg:block"><span class="inline-block">学生が主体となって取材し、</span><span class="inline-block">学び、</span><span class="inline-block">未来の物流を共に考えていきます。</span>
            </p>
            <div class="flex flex-col sm:flex-row gap-4 items-center justify-center w-full max-w-md sm:max-w-none">
                <a href="{FILE_ARCHIVE}" class="w-full sm:w-auto group inline-flex items-center justify-center gap-2 bg-[#D12442] hover:bg-[#B81C38] text-white font-bold px-8 py-4 rounded-xl transition-all duration-300 shadow-[0_4px_20px_rgba(209,36,66,0.4)] hover:shadow-[0_8px_30px_rgba(209,36,66,0.6)] transform hover:-translate-y-0.5 text-sm md:text-base">
                    <span>取材記事を読む</span> <i class="fa-solid fa-arrow-right transition-transform group-hover:translate-x-1"></i>
                </a>
                <a href="#features" class="w-full sm:w-auto group inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 border border-white/20 text-white font-bold px-8 py-4 rounded-xl transition-all duration-300 transform hover:-translate-y-0.5 text-sm md:text-base">
                    <span>詳細を見る</span>
                    <i class="fa-solid fa-chevron-down transition-transform group-hover:translate-y-1"></i>
                </a>
            </div>
        </div>
        
        <!-- スクロールインジケーター -->
        <div class="absolute bottom-6 left-1/2 transform -translate-x-1/2 flex flex-col items-center gap-1.5 animate-bounce">
            <span class="text-[9px] uppercase tracking-widest text-slate-400">Scroll Down</span>
            <i class="fa-solid fa-chevron-down text-slate-400 text-xs"></i>
        </div>
    </div>

    <!-- メインコンテンツコンテナ (画面幅にフィットするように最大幅を max-w-7xl に拡張) -->
    <main id="features" class="max-w-7xl mx-auto px-6 lg:px-8 py-16 space-y-16 relative z-10">
        
        <!-- ③ 特徴カード（3カラム横並び、幅広対応、境界線明確化） -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8" data-aos="fade-up">
            <!-- Card 1 -->
            <div class="bg-white p-8 rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] border border-slate-200 hover:border-[#002D5B]/30 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group flex flex-col justify-between">
                <div>
                    <div class="flex items-center gap-4 mb-4 shrink-0">
                        <div class="w-12 h-12 rounded-xl bg-[#9E1B32]/10 flex items-center justify-center text-[#9E1B32] text-xl shrink-0 group-hover:scale-110 transition-transform duration-300">
                            <i class="fa-solid fa-microphone-lines"></i>
                        </div>
                        <h3 class="text-lg font-bold text-slate-900 group-hover:text-[#002D5B] transition-colors leading-snug">現場のリアルを届ける。</h3>
                    </div>
                    <p class="text-slate-600 text-sm leading-relaxed">教科書的な知識に留まらず、企業の物流担当者が実際に直面している課題や、泥臭い現場のリアルな状況をインタビューします。</p>
                </div>
            </div>
            
            <!-- Card 2 -->
            <div class="bg-white p-8 rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] border border-slate-200 hover:border-[#002D5B]/30 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group flex flex-col justify-between">
                <div>
                    <div class="flex items-center gap-4 mb-4 shrink-0">
                        <div class="w-12 h-12 rounded-xl bg-[#002D5B]/10 flex items-center justify-center text-[#002D5B] text-xl shrink-0 group-hover:scale-110 transition-transform duration-300">
                            <i class="fa-solid fa-graduation-cap"></i>
                        </div>
                        <h3 class="text-lg font-bold text-slate-900 group-hover:text-[#002D5B] transition-colors leading-snug">学術的な視点で物流を見る。</h3>
                    </div>
                    <p class="text-slate-600 text-sm leading-relaxed">早稲田大学での数理最適化やシミュレーション研究の知見を背景に、学術と現場のギャップを見ていきます。</p>
                </div>
            </div>
            
            <!-- Card 3 -->
            <div class="bg-white p-8 rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] border border-slate-200 hover:border-[#002D5B]/30 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group flex flex-col justify-between">
                <div>
                    <div class="flex items-center gap-4 mb-4 shrink-0">
                        <div class="w-12 h-12 rounded-xl bg-[#9E1B32]/10 flex items-center justify-center text-[#9E1B32] text-xl shrink-0 group-hover:scale-110 transition-transform duration-300">
                            <i class="fa-solid fa-rocket"></i>
                        </div>
                        <h3 class="text-lg font-bold text-slate-900 group-hover:text-[#002D5B] transition-colors leading-snug">産学をつなぐ架け橋となる。</h3>
                    </div>
                    <p class="text-slate-600 text-sm leading-relaxed">これからの物流業界を担う若い世代や研究者に向けて、最前線の企業の挑戦を発信し、物流への関心を集めて発展に貢献します。</p>
                </div>
            </div>
        </div>

        <!-- 下部の最新取材記事・ポッドキャスト -->
        <div class="space-y-6" data-aos="fade-up" data-aos-delay="100">
            <div class="border-b-2 border-[#002D5B] pb-3 flex items-center gap-2">
                <span class="w-1.5 h-6 bg-[#9E1B32] rounded-full"></span>
                <h3 class="text-xl font-bold text-[#002D5B]">最新取材記事・ポッドキャスト</h3>
            </div>
            
            <!-- ======================================================================= -->
            <!-- 【管理用コメント】 -->
            <!-- 記事を追加する場合は、以下のグリッド(div)の中にカード(aタグ)をコピーして追加・編集してください。 -->
            <!-- ======================================================================= -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">

                <!-- 記事カードテンプレート (ここからコピー) -->
                <a href="{FILE_ARCHIVE}" class="block bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] border border-slate-200 overflow-hidden hover:shadow-xl hover:border-[#9E1B32]/20 hover:-translate-y-1 transition-all duration-300 group">
                    <div class="h-48 bg-gradient-to-br from-slate-100 to-slate-200 relative flex items-center justify-center text-slate-400 overflow-hidden">
                        <div class="absolute inset-0 bg-slate-900/5 group-hover:bg-slate-900/0 transition-colors duration-300"></div>
                        <i class="fa-solid fa-ship text-5xl text-[#002D5B]/70 group-hover:scale-110 transition-transform duration-500"></i>
                        <span class="absolute top-3 left-3 bg-[#002D5B] text-white text-[10px] px-2.5 py-1 rounded-full font-bold uppercase tracking-wider">飲料メーカー</span>
                    </div>
                    <div class="p-6">
                        <span class="text-[11px] text-slate-400 font-semibold block mb-2">2026.05.25</span>
                        <h4 class="text-lg font-bold text-slate-900 line-clamp-2 group-hover:text-[#9E1B32] transition-colors leading-snug">
                            【取材】製造と物流の同期化が生む、サプライチェーン全体の最適化プロセス
                        </h4>
                        <div class="mt-4 text-sm text-[#9E1B32] font-semibold flex items-center gap-1 group-hover:gap-2 transition-all">
                            <span>詳しく読む</span> <i class="fa-solid fa-arrow-right text-[11px]"></i>
                        </div>
                    </div>
                </a>
                <!-- 記事カードテンプレート (ここまでコピー) -->

                <!-- 予告/COMING SOONテンプレート -->
                <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] border border-slate-200 overflow-hidden opacity-75 relative group">
                    <div class="h-48 bg-slate-100 relative flex items-center justify-center text-slate-300">
                        <i class="fa-solid fa-truck-ramp-box text-5xl text-slate-300"></i>
                        <span class="absolute top-3 left-3 bg-slate-500 text-white text-[10px] px-2.5 py-1 rounded-full font-bold uppercase tracking-wider">鉄鋼・重機</span>
                        <div class="absolute inset-0 bg-white/20 backdrop-blur-[1px] flex items-center justify-center">
                            <span class="bg-slate-900/70 text-white text-xs px-4 py-1.5 rounded-full font-bold flex items-center gap-1.5 shadow-md">
                                <i class="fa-solid fa-lock text-[10px]"></i> 順次公開予定
                            </span>
                        </div>
                    </div>
                    <div class="p-6">
                        <span class="text-[11px] text-slate-400 font-semibold block mb-2">COMING SOON</span>
                        <h4 class="text-lg font-bold text-slate-500 line-clamp-2 leading-snug">
                            【次回予告】運行管理システムがもたらす、トラック運行効率化の現場
                        </h4>
                    </div>
                </div>

            </div>
        </div>
    </main>
"""

archive_content = f"""
    <main class="max-w-7xl mx-auto px-6 lg:px-8 py-12 min-h-[calc(100vh-160px)] relative z-10">
        <div x-data="{{ currentCategory: 'all' }}">
            <div class="border-b border-slate-200 pb-4 mb-6">
                <h2 class="text-2xl font-bold text-[#002D5B]">取材実績・記事アーカイブ</h2>
                <p class="text-slate-500 text-sm mt-1">各企業の物流担当者へのインタビュー記事一覧</p>
            </div>

            <div class="flex flex-wrap gap-2 mb-6 text-xs font-bold">
                <button @click="currentCategory = 'all'" :class="currentCategory === 'all' ? 'bg-[#002D5B] text-white' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'" class="px-3.5 py-2 rounded-xl transition-all shadow-sm cursor-pointer">すべて</button>
                <button @click="currentCategory = 'food'" :class="currentCategory === 'food' ? 'bg-[#002D5B] text-white' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'" class="px-3.5 py-2 rounded-xl transition-all shadow-sm cursor-pointer">食品・飲料</button>
                <button @click="currentCategory = 'steel'" :class="currentCategory === 'steel' ? 'bg-[#002D5B] text-white' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'" class="px-3.5 py-2 rounded-xl transition-all shadow-sm cursor-pointer">鉄鋼・重機</button>
                <button @click="currentCategory = 'tech'" :class="currentCategory === 'tech' ? 'bg-[#002D5B] text-white' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'" class="px-3.5 py-2 rounded-xl transition-all shadow-sm cursor-pointer">IT・自動運転</button>
            </div>

            <!-- ======================================================================= -->
            <!-- 【管理用コメント】 -->
            <!-- 記事を追加する場合は、以下のグリッド(div)の中にカードをコピーして追加・編集してください。 -->
            <!-- ======================================================================= -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- 記事カードテンプレート (ここからコピー) -->
                <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] overflow-hidden border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group" x-show="currentCategory === 'all' || currentCategory === 'food'" data-aos="fade-up" data-aos-delay="100">
                    <div class="h-48 bg-gradient-to-br from-slate-100 to-slate-200 relative flex items-center justify-center text-slate-400 overflow-hidden">
                        <div class="absolute inset-0 bg-slate-900/5 group-hover:bg-slate-900/0 transition-colors duration-300"></div>
                        <i class="fa-solid fa-ship text-4xl text-[#002D5B]/70 group-hover:scale-110 transition-transform duration-500"></i>
                        <span class="absolute top-3 left-3 bg-[#002D5B] text-white text-[10px] px-2.5 py-1 rounded-full font-bold uppercase tracking-wider">飲料メーカー</span>
                    </div>
                    <div class="p-6">
                        <span class="text-xs text-slate-400 block mb-2 font-semibold">2026.05.25</span>
                        <h3 class="text-lg font-bold text-slate-900 mb-2 group-hover:text-[#9E1B32] transition-colors leading-snug cursor-pointer">
                            【取材】製造と物流の同期化が生む、サプライチェーン全体の最適化プロセス
                        </h3>
                        <p class="text-slate-600 text-xs leading-relaxed line-clamp-3 mb-4">
                            需要予測の変動に対して、いかにして配車計画と拠点在庫を動的にコントロールするのか。現場の意思決定に迫ります。
                        </p>
                        <div class="flex flex-wrap gap-1.5">
                            <span class="bg-slate-50 text-slate-500 text-[10px] px-2.5 py-1 rounded-full font-medium border border-slate-100">配送最適化</span>
                            <span class="bg-slate-50 text-slate-500 text-[10px] px-2.5 py-1 rounded-full font-medium border border-slate-100">拠点配置</span>
                        </div>
                    </div>
                </div>
                <!-- 記事カードテンプレート (ここまでコピー) -->

                <!-- 予告/COMING SOONテンプレート -->
                <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] overflow-hidden border border-slate-200 opacity-75 relative group" x-show="currentCategory === 'all' || currentCategory === 'steel' || currentCategory === 'tech'" data-aos="fade-up" data-aos-delay="200">
                    <div class="h-48 bg-slate-100 relative flex items-center justify-center text-slate-300">
                        <i class="fa-solid fa-truck-ramp-box text-4xl text-slate-300"></i>
                        <span class="absolute top-3 left-3 bg-slate-500 text-white text-[10px] px-2.5 py-1 rounded-full font-bold uppercase tracking-wider">鉄鋼・重機</span>
                        <div class="absolute inset-0 bg-white/20 backdrop-blur-[1.5px] flex items-center justify-center">
                            <span class="bg-slate-900/70 text-white text-xs px-4 py-1.5 rounded-full font-bold flex items-center gap-1.5 shadow-md">
                                <i class="fa-solid fa-lock text-[11px]"></i> 順次公開予定
                            </span>
                        </div>
                    </div>
                    <div class="p-6">
                        <span class="text-xs text-slate-400 block mb-2 font-semibold">COMING SOON</span>
                        <h3 class="text-lg font-bold text-slate-400 mb-2 leading-snug">
                            【次回予告】運行管理システムがもたらす、トラック運行効率化の現場
                        </h3>
                        <p class="text-slate-400 text-xs leading-relaxed line-clamp-3">
                            自動運転や幹線輸送の共同運行、鉄鋼重機輸送を視野に入れた、次世代のスケジューリングについての取材を予定しています。
                        </p>
                    </div>
                </div>

            </div>
        </div>
    </main>
"""

profile_content = f"""
    <main class="max-w-7xl mx-auto px-6 lg:px-8 py-12 min-h-[calc(100vh-160px)] relative z-10">
        <div class="space-y-12">
            <div class="border-b border-slate-200 pb-4">
                <h2 class="text-2xl font-bold text-[#002D5B]">運営者プロフィール</h2>
            </div>

            <!-- プロジェクト概要セクション -->
            <div class="space-y-4">
                <div class="border-l-4 border-[#002D5B] pl-3">
                    <h3 class="text-lg font-bold text-[#002D5B]">プロジェクト概要</h3>
                </div>
                <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] p-8 border border-slate-200 hover:shadow-lg transition-all duration-300" data-aos="fade-up" data-aos-delay="100">
                    <div class="flex items-center space-x-4 mb-6">
                        <div class="w-24 md:w-32 shrink-0 overflow-hidden rounded-xl border border-slate-200 shadow-sm bg-white p-1">
                            <img src="../images/LOGO.jpg" alt="LOGISTICS FRONTIER INTERVIEWS" class="w-full h-auto object-contain">
                        </div>
                        <div>
                            <h4 class="text-lg font-bold text-slate-900">蓮池研究室 SC情報発信プロジェクト</h4>
                            <p class="text-xs text-[#9E1B32] font-semibold font-poppins">Supply Chain Research Lab Project</p>
                        </div>
                    </div>
                    <div class="text-slate-600 text-sm leading-relaxed space-y-4">
                        <p>私たちは、早稲田大学・蓮池研究室で数理最適化やシミュレーションを用いて物流研究を行っているメンバーと、共同研究先である鉄鋼系運送会社（メタル便）の有志メンバーで構成されています。本プロジェクトでは、日本物流の発展に向けて、<strong>SC（サプライチェーン：Supply Chain）</strong>の現場の実態や、最前線で物流を支えてきた先人たちの貴重な「知」と「経験」を後世（次代）へ継承・発信していくことを目的としています。この情報発信活動を通じて、学生自身にとっても実務的な知見や多様な視点を獲得し、深い学びを得るための自主プロジェクトとして活動しています。</p>
                        <p>単に研究室に籠もるだけでなく、現場調査（フィールドワーク）を通じて実社会の物流効率化・2024年問題をはじめとする社会的課題にコミットすることを目指しています。</p>
                        <div class="pt-4 border-t border-slate-100 flex flex-wrap gap-4">
                            <a href="https://hasuikelab.w.waseda.jp/" target="_blank" class="inline-flex items-center space-x-1 text-xs text-[#002D5B] font-bold hover:text-[#9E1B32] hover:underline transition-colors">
                                <span>蓮池研究室 公式サイト</span> <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                            </a>
                            <a href="https://www.metalbin.net/" target="_blank" class="inline-flex items-center space-x-1 text-xs text-[#9E1B32] font-bold hover:text-[#002D5B] hover:underline transition-colors">
                                <span>メタル便 公式サイト</span> <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ④ アドバイザー セクション -->
            <div class="space-y-4">
                <div class="border-l-4 border-[#9E1B32] pl-3">
                    <h3 class="text-xl font-bold text-[#002D5B] tracking-wider">アドバイザー</h3>
                </div>
                
                <!-- 梶大吉氏カード -->
                <div class="max-w-3xl bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] p-8 border border-slate-200 hover:shadow-lg transition-all duration-300 flex flex-col justify-between" data-aos="fade-up" data-aos-delay="200">
                    <div>
                        <div class="flex items-center space-x-4 mb-6">
                            <div class="w-20 h-20 rounded-full shrink-0 shadow-sm border border-slate-200 overflow-hidden bg-slate-200 ring-4 ring-slate-100">
                                <img src="../images/Kaji.jpg" alt="梶 大吉" class="w-full h-full object-cover object-center">
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-slate-900">梶 大吉</h4>
                                <p class="text-xs text-[#002D5B] font-semibold font-poppins">1979年慶應義塾大学商学部卒/総合トラック（株）代表取締役/（株）メタル便代表取締役</p>
                            </div>
                        </div>
                        <div class="text-slate-600 text-sm leading-relaxed space-y-3">
                            <p>1979年に慶応義塾大学商学部を卒業後、運送事業に携わり、総合トラック株式会社および株式会社メタル便の代表取締役に就任。</p>
                            <p>2000年には日本初となる鋼材の混載ビジネスを「メタル便」として千葉県浦安市にて立ち上げました。現在は全国の物流会社8社のネットワークにより、長尺・異形状貨物の全国への混載輸送を展開しています。</p>
                            <p>2016年にはメタル便グループとして、事業継続（BCP）における優れた取り組みが評価され、「BCAOアワード特別賞」および「最優秀実践賞」をダブル受賞しました。</p>
                            <p>2021年、自身の病気療養を機に経営執行を次世代へ委譲。現在は、物流業界の発展と次世代の人材育成、さらには産学連携活動の推進に注力しています。</p>
                        </div>
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border-l-4 border-[#9E1B32] shadow-inner text-xs mt-6">
                        <strong class="text-slate-800 block mb-2"><i class="fa-solid fa-briefcase mr-1 text-[#9E1B32]"></i>主な経歴・役職・共同研究：</strong>
                        <ul class="list-disc list-inside space-y-1 text-slate-600 ml-1">
                            <li>総合トラック株式会社 代表取締役</li>
                            <li>株式会社メタル便 代表取締役</li>
                            <li>2026年〜：慶應義塾大学 高度物流人材育成塾 理事</li>
                            <li>2026年〜：早稲田大学 蓮池研究室 共同研究中</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- ④ 活動学生 セクション -->
            <div class="space-y-4">
                <div class="border-l-4 border-[#002D5B] pl-3">
                    <h3 class="text-xl font-bold text-[#002D5B] tracking-wider">活動学生</h3>
                </div>
                
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <!-- 長野恵治氏カード -->
                    <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] p-8 border border-slate-200 hover:shadow-lg transition-all duration-300 flex flex-col justify-between" data-aos="fade-up" data-aos-delay="300">
                        <div>
                            <div class="flex items-center space-x-4 mb-6">
                                <div class="w-20 h-20 rounded-full shrink-0 shadow-sm border border-slate-200 overflow-hidden bg-slate-200 ring-4 ring-slate-100">
                                    <img src="../images/Keiji.jpeg" alt="長野 恵治" class="w-full h-full object-cover object-center">
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-slate-900">長野 恵治</h4>
                                    <p class="text-xs text-[#002D5B] font-semibold font-poppins">早稲田大学院　創造理工学研究科　経営システム工学専攻　修士2年</p>
                                </div>
                            </div>
                            <div class="text-slate-600 text-sm leading-relaxed space-y-3">
                                <p>学部生時代はスポーツメディアの運営に携わり、大学ラグビー部への現地取材や試合記事執筆、プロジェクト管理などの発信活動を精力的に行ってきました。</p>
                                <p>研究活動では、物流の「2024年問題」をきっかけに日本のサプライチェーンに興味を抱き、卒業研究では卸売市場での現地調査（フィールドワーク）を行い、プログラミングを用いた荷待ち時間削減のシミュレーションを構築し、国際学会での発表を経験。現在は大学院にて、災害時の道路寸断リスクを考慮した強靭な「拠点配置計画」の数理最適化モデルを研究しています。</p>
                                <p>本プロジェクトを通じて、今後も物流に携わる身として、実務家の方々の視点や意見から学びを得て、物流業界に影響を与えることができる人材を目指しています。</p>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-4 rounded-xl border-l-4 border-[#9E1B32] shadow-inner text-xs mt-6">
                            <strong class="text-slate-800 block mb-2"><i class="fa-solid fa-magnifying-glass-chart mr-1 text-[#9E1B32]"></i>主な研究関心：</strong>
                            <ul class="list-disc list-inside space-y-1 text-slate-600 ml-1">
                                <li>学部研究：トラックの待機時間削減に向けた荷役・バース運用のシミュレーション</li>
                                <li>災害時のルーティング最適化</li>
                                <li>拠点最適化モデルの構築</li>
                            </ul>
                        </div>
                    </div>

                    <!-- 安井佑夢氏カード -->
                    <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] p-8 border border-slate-200 hover:shadow-lg transition-all duration-300 flex flex-col justify-between" data-aos="fade-up" data-aos-delay="400">
                        <div>
                            <div class="flex items-center space-x-4 mb-6">
                                <div class="w-20 h-20 rounded-full shrink-0 shadow-sm border border-slate-200 overflow-hidden bg-slate-200 ring-4 ring-slate-100">
                                    <img src="../images/Yumu.jpeg" alt="安井 佑夢" class="w-full h-full object-cover object-center">
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-slate-900">安井 佑夢</h4>
                                    <p class="text-xs text-[#002D5B] font-semibold font-poppins">早稲田大学院　創造理工学研究科　経営システム工学専攻　修士2年</p>
                                </div>
                            </div>
                            <div class="text-slate-600 text-sm leading-relaxed space-y-3">
                                <p>学部生時代は理工展連絡会の財務局長兼会計として学園祭の運営に携わりました。</p>
                                <p>研究活動では2024年問題に代表される物流課題の解決として移動販売に着目し、各地点の需要が不確実な配送計画問題ついて輸送コストと需要量充足のトレードオフを満たすモデルを提案し、国際学会で発表を行いました。修士では回収も含めた配送計画問題についての研究を行う予定です。</p>
                                <p>本プロジェクトを通じて、社会人として重要となる視座や考え方を身につけたいと考えています。</p>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-4 rounded-xl border-l-4 border-[#9E1B32] shadow-inner text-xs mt-6">
                            <strong class="text-slate-800 block mb-2"><i class="fa-solid fa-magnifying-glass-chart mr-1 text-[#9E1B32]"></i>主な研究関心：</strong>
                            <ul class="list-disc list-inside space-y-1 text-slate-600 ml-1">
                                <li>学部研究：巡回セールスマン問題の新たな定式化の提案</li>
                                <li>確率を用いた意思決定支援</li>
                                <li>配送計画問題の最適化</li>
                            </ul>
                        </div>
                    </div>

                    <!-- 井上聡太氏カード -->
                    <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] p-8 border border-slate-200 hover:shadow-lg transition-all duration-300 flex flex-col justify-between" data-aos="fade-up" data-aos-delay="500">
                        <div>
                            <div class="flex items-center space-x-4 mb-6">
                                <div class="w-20 h-20 rounded-full shrink-0 shadow-sm border border-slate-200 overflow-hidden bg-slate-200 ring-4 ring-slate-100">
                                    <img src="../images/Sota.jpeg" alt="井上 聡太" class="w-full h-full object-cover object-center">
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-slate-900">井上 聡太</h4>
                                    <p class="text-xs text-[#002D5B] font-semibold font-poppins">早稲田大学院　創造理工学研究科　経営システム工学専攻　修士1年</p>
                                </div>
                            </div>
                            <div class="text-slate-600 text-sm leading-relaxed space-y-3">
                                <p>学部生時代は、他学部にて計量経済学を学びました。その中で、社会全体を俯瞰するだけでなく、より現場に根差した視点から社会課題に向き合いたいと考え、大学院から経営システム工学を専攻しています。</p>
                                <p>現在はエージェントベースモデルを用いた社会シミュレーションを学んでおり、京都市におけるオーバーツーリズム問題について研究を行う予定です。</p>
                                <p>物流業界については、不安定な社会情勢や規制の強化により、数理的アプローチの必要性が高まっていると感じています。本プロジェクトでは、物流の現場から見える課題を学び、物流業界への理解と関心を深め、自身が提供できる価値について考えていきたいです。</p>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-4 rounded-xl border-l-4 border-[#9E1B32] shadow-inner text-xs mt-6">
                            <strong class="text-slate-800 block mb-2"><i class="fa-solid fa-magnifying-glass-chart mr-1 text-[#9E1B32]"></i>主な研究関心：</strong>
                            <ul class="list-disc list-inside space-y-1 text-slate-600 ml-1">
                                <li>エージェントベースモデルを用いた社会シミュレーション</li>
                                <li>京都市におけるオーバーツーリズム問題の分析</li>
                                <li>物流課題に対する数理的アプローチ</li>
                            </ul>
                        </div>
                    </div>

                    <!-- 上村まどか氏カード -->
                    <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] p-8 border border-slate-200 hover:shadow-lg transition-all duration-300 flex flex-col justify-between" data-aos="fade-up" data-aos-delay="600">
                        <div>
                            <div class="flex items-center space-x-4 mb-6">
                                <div class="w-20 h-20 rounded-full shrink-0 shadow-sm border border-slate-200 overflow-hidden bg-slate-200 ring-4 ring-slate-100">
                                    <img src="../images/Madoka.jpg" alt="上村 まどか" class="w-full h-full object-cover object-center">
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-slate-900">上村 まどか</h4>
                                    <p class="text-xs text-[#002D5B] font-semibold font-poppins">早稲田大学　創造理工学部　経営システム工学科　4年</p>
                                </div>
                            </div>
                            <div class="text-slate-600 text-sm leading-relaxed space-y-3">
                                <p>現在、早稲田大学の学部4年生として経営システム工学を専攻しています。実社会の課題解決に向けたアプローチを学んでおり、物流分野への応用に関心を持っています。</p>
                                <p>本プロジェクトを通じて、現場の実情に触れ、理論と実践を結びつける視点を身につけたいと考えています。</p>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-4 rounded-xl border-l-4 border-[#9E1B32] shadow-inner text-xs mt-6">
                            <strong class="text-slate-800 block mb-2"><i class="fa-solid fa-magnifying-glass-chart mr-1 text-[#9E1B32]"></i>主な研究関心：</strong>
                            <ul class="list-disc list-inside space-y-1 text-slate-600 ml-1">
                                <li>物流現場の課題分析</li>
                                <li>システム工学の社会応用</li>
                            </ul>
                        </div>
                    </div>

                    <!-- 谷口結氏カード -->
                    <div class="bg-white rounded-2xl shadow-[0_4px_25px_rgba(0,0,0,0.03)] p-8 border border-slate-200 hover:shadow-lg transition-all duration-300 flex flex-col justify-between" data-aos="fade-up" data-aos-delay="700">
                        <div>
                            <div class="flex items-center space-x-4 mb-6">
                                <div class="w-20 h-20 rounded-full shrink-0 shadow-sm border border-slate-200 overflow-hidden bg-slate-200 ring-4 ring-slate-100">
                                    <img src="../images/yui.jpeg" alt="谷口 結" class="w-full h-full object-cover object-center">
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-slate-900">谷口 結</h4>
                                    <p class="text-xs text-[#002D5B] font-semibold font-poppins">早稲田大学　創造理工学部　経営システム工学科　4年</p>
                                </div>
                            </div>
                            <div class="text-slate-600 text-sm leading-relaxed space-y-3">
                                <p>学部で物流システムや倉庫レイアウト設計について学ぶ中で、物流は企業活動を支える重要な社会基盤であり、多くの課題を抱える分野であることを実感しました。</p>
                                <p>本活動を通じて、企業が直面する物流課題への理解を深めるとともに、多角的な視点と実践的な思考力を身につけ、課題解決に主体的に取り組める力を養いたいと考えています。</p>
                            </div>
                        </div>
                        <div class="bg-slate-50 p-4 rounded-xl border-l-4 border-[#9E1B32] shadow-inner text-xs mt-6">
                            <strong class="text-slate-800 block mb-2"><i class="fa-solid fa-magnifying-glass-chart mr-1 text-[#9E1B32]"></i>主な研究関心：</strong>
                            <ul class="list-disc list-inside space-y-1 text-slate-600 ml-1">
                                <li>シミュレーションを用いた大規模施設の混雑緩和</li>
                                <li>倉庫レイアウト設計・最適化</li>
                                <li>物流システムの最適化</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
"""

contact_content = f"""
    <main class="max-w-4xl mx-auto px-6 lg:px-8 py-12 min-h-[calc(100vh-160px)] relative z-10">
        <div class="border-b border-slate-200 pb-4 mb-6">
            <h2 class="text-2xl font-bold text-[#002D5B]">取材のお申し込み・お問い合わせ</h2>
            <p class="text-slate-500 text-sm mt-1">企業の物流担当者様、広報担当者様からのご連絡をお待ちしております</p>
        </div>

        <div class="bg-white rounded-2xl shadow-sm p-6 md:p-8 border border-slate-100" x-data="{{ formSubmitted: false, errorMessage: '' }}">
            <div x-show="formSubmitted" class="text-center py-12" x-transition>
                <div class="text-emerald-500 text-5xl mb-4"><i class="fa-solid fa-circle-check"></i></div>
                <h3 class="text-xl font-bold mb-2 text-slate-900">送信が完了しました</h3>
                <p class="text-slate-600 text-sm mb-6">内容を確認の上、大学のメールアドレスより3営業日以内に折り返しご連絡いたします。</p>
            </div>

            <div x-show="errorMessage" class="bg-red-50 text-red-600 p-3 rounded-lg text-xs font-bold mb-4" x-text="errorMessage"></div>

            <form x-show="!formSubmitted" action="https://formspree.io/f/xdajpjjg" method="POST" 
                  @submit.prevent="
                    fetch($el.action, {{
                        method: 'POST',
                        body: new FormData($el),
                        headers: {{ 'Accept': 'application/json' }}
                    }})
                    .then(response => {{
                        if (response.ok) {{
                            formSubmitted = true;
                            errorMessage = '';
                        }} else {{
                            errorMessage = '送信に失敗しました。時間をおいて再度お試しください。';
                        }}
                    }})
                    .catch(error => {{ errorMessage = '通信エラーが発生しました。'; }})
                  " class="space-y-5">
                
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-2">貴社名 / 組織名 <span class="text-[#9E1B32]">*</span></label>
                    <input type="text" name="company" required class="w-full px-4 py-2.5 text-sm border border-slate-300 rounded-xl focus:outline-none focus:border-[#002D5B] focus:ring-1 focus:ring-[#002D5B] bg-slate-50 transition-all" placeholder="例）〇〇株式会社 物流統括部">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-2">お名前 <span class="text-[#9E1B32]">*</span></label>
                    <input type="text" name="name" required class="w-full px-4 py-2.5 text-sm border border-slate-300 rounded-xl focus:outline-none focus:border-[#002D5B] focus:ring-1 focus:ring-[#002D5B] bg-slate-50 transition-all" placeholder="例）山田 太郎">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-2">メールアドレス <span class="text-[#9E1B32]">*</span></label>
                    <input type="email" name="_replyto" required class="w-full px-4 py-2.5 text-sm border border-slate-300 rounded-xl focus:outline-none focus:border-[#002D5B] focus:ring-1 focus:ring-[#002D5B] bg-slate-50 transition-all" placeholder="例）yamada@example.com">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-2">お問い合わせ内容の分類 <span class="text-[#9E1B32]">*</span></label>
                    <select name="category" class="w-full px-4 py-2.5 text-sm border border-slate-300 rounded-xl focus:outline-none focus:border-[#002D5B] bg-slate-50 text-slate-600 transition-all">
                        <option value="取材の受け入れについて">取材の受け入れについて</option>
                        <option value="共同研究・意見交換のご相談">共同研究・意見交換のご相談</option>
                        <option value="その他のお問い合わせ">その他のお問い合わせ</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-2">メッセージ本文 <span class="text-[#9E1B32]">*</span></label>
                    <textarea name="message" required rows="4" class="w-full px-4 py-2.5 text-sm border border-slate-300 rounded-xl focus:outline-none focus:border-[#002D5B] focus:ring-1 focus:ring-[#002D5B] bg-slate-50 transition-all" placeholder="取材を許可いただける場合、お話が可能な範囲や現在の課題感などをご記入いただけますと幸いです。"></textarea>
                </div>
                <div class="text-[11px] text-slate-400 bg-slate-100 p-3 rounded-lg border border-slate-200">
                    ※ご記入いただいた個人情報および企業秘密は、学術研究および本発信メディアの運営目的以外には一切使用いたしません。
                </div>
                <button type="submit" class="w-full bg-[#002D5B] hover:bg-slate-800 text-white font-bold py-3 rounded-xl transition-all text-sm shadow hover:shadow-lg">
                    入力内容を送信する
                </button>
            </form>
        </div>
    </main>
"""

# Ensure the output directory exists
os.makedirs("pages", exist_ok=True)

with open(os.path.join("pages", FILE_TOP), "w", encoding="utf-8") as f:
    f.write(get_header("top") + top_content + get_footer("top"))

with open(os.path.join("pages", FILE_ARCHIVE), "w", encoding="utf-8") as f:
    f.write(get_header("archive") + archive_content + get_footer("archive"))

with open(os.path.join("pages", FILE_PROFILE), "w", encoding="utf-8") as f:
    f.write(get_header("profile") + profile_content + get_footer("profile"))

with open(os.path.join("pages", FILE_CONTACT), "w", encoding="utf-8") as f:
    f.write(get_header("contact") + contact_content + get_footer("contact"))

print("【大成功】キャッチコピーと文言の調整、および大学の公式主張制限に配慮した更新を行いました！")
