%%
%% This is file `poli.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% poli.dtx  (with options: `class')
%% 
%% This is the `poli' document class used for composition of LaTeX
%% monographs (master and PhD thesis, and PhD qualifying exams)
%% satisfying the requirements of the Coordination of Research and
%% Graduate Courses in Engineering at the Federal University of
%% Rio de Janeiro.
%% 
%% Copyright (C) 2008 Vicente Helano and George Ainsworth Jr.
%% 
%% This program is free software; you can redistribute it and/or modify
%% it under the terms of the GNU General Public License version 3 as
%% published by the Free Software Foundation.
%% 
%% This program is distributed in the hope that it will be useful,
%% but WITHOUT ANY WARRANTY; without even the implied warranty of
%% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
%% GNU General Public License version 3 for more details.
%% 
%% You should have received a copy of the GNU General Public License
%% version 3 along with this package (see COPYING file).
%% If not, see <http://www.gnu.org/licenses/>.
%% 
%% Author(s): Vicente Helano,
%%            George Ainsworth
%% 
%% \CheckSum{1309}
%% \CharacterTable
%%  {Upper-case    \A\B\C\D\E\F\G\H\I\J\K\L\M\N\O\P\Q\R\S\T\U\V\W\X\Y\Z
%%   Lower-case    \a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z
%%   Digits        \0\1\2\3\4\5\6\7\8\9
%%   Exclamation   \!     Double quote  \"     Hash (number) \#
%%   Dollar        \$     Percent       \%     Ampersand     \&
%%   Acute accent  \'     Left paren    \(     Right paren   \)
%%   Asterisk      \*     Plus          \+     Comma         \,
%%   Minus         \-     Point         \.     Solidus       \/
%%   Colon         \:     Semicolon     \;     Less than     \<
%%   Equals        \=     Greater than  \>     Question mark \?
%%   Commercial at \@     Left bracket  \[     Backslash     \\
%%   Right bracket \]     Circumflex    \^     Underscore    \_
%%   Grave accent  \`     Left brace    \{     Vertical bar  \|
%%   Right brace   \}     Tilde         \~}
%%
\def\filename{poli.dtx}
\def\fileversion{v2.0}
\def\filedate{2007/03/01}
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{poli}[\filedate\ \fileversion\ Poli Dissertations]
\LoadClass[12pt,a4paper,oneside]{book}
\RequirePackage{lastpage}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage[english,brazil]{babel}
\RequirePackage{hyphenat}
\RequirePackage{ifthen}
\RequirePackage{graphicx}
\RequirePackage{tabularx}
\RequirePackage{eqparbox}
\RequirePackage[a4paper,bindingoffset=0.0cm,vcentering=true,%
top=2.5cm,bottom=2.5cm,left=3.0cm,right=3.0cm]{geometry}
\def\CoppeTeX{{\rm C\kern-.05em{\sc o\kern-.025em p\kern-.025em
			p\kern-.025em e}}\kern-.08em\TeX}
\renewcommand\baselinestretch{1.5}
\let\@adname\@empty
\let\@adsurn\@empty
\let\@coadname\@empty
\let\@coadsurn\@empty
\newcounter{minexaminers}
\newboolean{isdraft}
\newboolean{maledoc}
\setboolean{maledoc}{false}
\setboolean{isdraft}{false}
\newboolean{needbb}
\setboolean{needbb}{false}
\DeclareOption{grad}{%
	\newcommand{\@degree}{M.Sc.}
	\newcommand{\@degreename}{Graduação}
	\newcommand{\local@degname}{Engenheiro}
	\newcommand{\foreign@degname}{Engineer}
	\newcommand\local@doctype{Projeto}
	\newcommand\foreign@doctype{Undergraduate Project}
	\setcounter{minexaminers}{2}
}
\DeclareOption{draft}{%
	\setboolean{isdraft}{true}
	\ClassWarning{poli}{draft mode is ON}%
}
\DeclareOption{dvips}{%
	\PassOptionsToPackage{dvips}{hyperref,graphicx}
}
\DeclareOption{dvipdfm}{%
	\PassOptionsToPackage{dvipdfm}{hyperref,graphicx}
	\setboolean{needbb}{true}
}
\DeclareOption{pdftex}{%
	\PassOptionsToPackage{pdftex}{hyperref,graphicx}
	\PassOptionsToPackage{plainpages=false,pdfpagelabels}{hyperref}
}
\ProcessOptions\relax
\newcommand\university[1]{%
	\renewcommand\local@universityname{#1}
}
\newcommand\department[1]{%
	\ifthenelse{\equal{#1}{DEE}}
	{\global\def\local@deptname{Engenharia Elétrica}
		\global\def\foreign@deptname{Electrical Engineering}
  	\global\def\local@jobname{Engenheiro de Controle e Automação}
		\global\def\foreign@jobname{Control and Automation Engineer}}   
}
\renewcommand\title[1]{%
	\global\def\local@title{#1}%
}
\newcommand\foreigntitle[1]{%
	\global\def\foreign@title{#1}%
}
\newcommand\advisor[4]{%
	\global\def\@adtitle{#1}%
	\global\def\@adname{#2}%
	\global\def\@adsurn{#3}%
	\global\def\@addegree{#4}%
}
\newcommand\coadvisor[4]{%
	\global\def\@coadtitle{#1}%
	\global\def\@coadname{#2}%
	\global\def\@coadsurn{#3}%
	\global\def\@coaddegree{#4}%
	\renewcommand\local@advisorstring{Orientadores}%
	\renewcommand\foreign@advisorstring{Advisors}%
}
\newcount\@examiner\@examiner0
\newcommand\examiner[3]{%
	\global\@namedef{S:\expandafter\the\@examiner}{#1\ #2, #3}
	\global\advance\@examiner by 1
}
\renewcommand\author[2]{%
	\global\def\@authname{#1}
	\global\def\@authsurn{#2}
}
\renewcommand\date[2]{%
	\month=#1
	\year=#2
}
\newcommand\local@monthname{\ifcase\month\or
	Janeiro\or Fevereiro\or Março\or Abril\or Maio\or Junho\or
	Julho\or Agosto\or Setembro\or Outubro\or Novembro\or Dezembro\fi}
\newcommand\foreign@monthname{\ifcase\month\or
	January\or February\or March\or April\or May\or June\or
	July\or August\or September\or October\or November\or December\fi}
\newcommand\place[3]{%
	\renewcommand\local@cityname{#1}
	\renewcommand\local@statename{#2}
	\renewcommand\local@countryname{#3}
}
\newcounter{keywords}
\newcommand\keyword[1]{%
	\global\@namedef{K:\expandafter\the\c@keywords}{#1}
	\global\addtocounter{keywords}{1}
}
\renewcommand\frontmatter{%
	\cleardoublepage
	\@mainmatterfalse
	\pagenumbering{roman}
	\thispagestyle{empty}
	\setcounter{page}{2}
	\makefrontpage
	\clearpage
	\pagestyle{plain}
	\ifthenelse{\boolean{maledoc}}{}{\makecatalog}%
}
\renewcommand\mainmatter{%
	\immediate\write\@auxout{%
		\string\newlabel{front:pageno}{{}{\Roman{page}}{}{page.\roman{page}}{}}}
	\cleardoublepage
	\@mainmattertrue
	\pagestyle{plain}
	\pagenumbering{arabic}}
\renewcommand\backmatter{%
	\if@openright
	\cleardoublepage
	\else
	\clearpage
	\fi}
\renewcommand\maketitle{%
	\pagenumbering{alph}
	\config@hypersetup
	\begin{titlepage}
		\begin{flushleft}
			\setlength\baselineskip{0pt}
			\setlength\parskip{1mm}
			\makebox[20mm][c]{%
				\includegraphics[width =0.5\linewidth]{Imagens/Logo_EPUFRJ_2020.png}}\par
		\end{flushleft}
		\begin{center}
			\nohyphens{\MakeUppercase\local@title}\par
			\vspace*{28mm}
			\nohyphens{\@authname\ \@authsurn}\par
		\end{center}
		\vspace*{16mm}
		\begin{flushright}
			\begin{minipage}{90mm}
				\frontcover@maintext
			\end{minipage}\par
			\vspace*{7.5mm}
			\begin{tabularx}{90mm}[b]{@{}l@{ }X@{}}
				\local@advisorstring: & \nohyphens{\@adname\ \@adsurn}\\
				\ifthenelse{\equal{\@coadname}{\@empty}}{}{%
					& \nohyphens{\@coadname\ \@coadsurn}\\}
			\end{tabularx}\par
		\end{flushright}
		\vspace*{\fill}
		\begin{center}
			\local@cityname\par
			\local@monthname\ de \number\year
		\end{center}
	\end{titlepage}
	\global\let\maketitle\relax%
	\global\let\and\relax}
\newcommand\makefrontpage{%
	\begin{center}
		\noindent% just to prevent indentation narrowing the line width for this line
		\includegraphics[width=0.15\textwidth]{Imagens/Logo_UFRJ.png}%
		\begin{minipage}[b]{0.7\textwidth}
			\centering
			\textit{\textbf{UNIVERSIDADE FEDERAL DO RIO DE JANEIRO}}\\
			\vspace{2 mm}
            \textbf{Escola Politécnica}\\
			Departamento de \local@deptname\\
		\end{minipage}%
		\includegraphics[width=0.35\textwidth]{Imagens/Logo_EPUFRJ_2020.png}\par
		\vspace*{10mm}
		\sloppy\nohyphens{\MakeUppercase\local@title}\par
		\vspace*{7mm}
		{\@authname\ \@authsurn}\par
	\end{center}\par
	\vspace*{4mm}
	\frontpage@maintext
	\vspace*{8mm}
	\noindent\local@approvedname:\par
	\begin{center}
		\begin{flushright}
			\vskip16\p@ \baselineskip12pt
			\eqparbox{signture@list}{\hrulefill}\\
			\eqparbox{signture@list}{\protect%\centering%
				\ \ \ \ \ \ \ \ \ \ \@adtitle\ \@adname\ \@adsurn, \@addegree\ \ \ \ \ \ \ \ \ \ }\\
			\ifthenelse{\equal{\@coadname}{\@empty}}{}{%
				\vskip26\p@ \baselineskip12pt
				\eqparbox{signture@list}{\hrulefill}\\
				\eqparbox{signture@list}{\protect%\centering%
					\ \ \ \ \ \ \ \ \ \ \@coadtitle\ \@coadname\ \@coadsurn, \@coaddegree\ \ \ \ \ \ \ \ \ \ }\\}
			\count1=0
			\@whilenum \count1<\@examiner \do {
				\vskip26\p@ \baselineskip12pt
				\eqparbox{signture@list}{\hrulefill}\\
				\eqparbox{signture@list}{\protect%\centering%
					\ \ \ \ \ \ \ \ \ \ \csname S:\the\count1 \endcsname\ \ \ \ \ \ \ \ \ \ }\\
				\advance\count1 by 1}
		\end{flushright}
	\end{center}
	\vspace*{\fill}
	\frontpage@bottomtext}
\newcommand\config@hypersetup{%
	\begingroup
	% changes to \toks@ and \count@ are kept local;
	% it's not necessary for them, but it is usually the case
	% for \count1, because the first ten counters are written
	% to the DVI file, thus you got lucky because of PDF output
	\toks@={}% in this special case not necessary
	\count@=0 %
	\@whilenum\count@<\value{keywords}\do{%
		% * a keyword separator is not necessary,
		%    if there is just one keyword
		% * \csname K:\the\count@\endcsname must be expanded
		%    at least once, to get rid of the loop depended \count@
		\ifcase\count@ % same as \ifnum0=\count@
		\toks@=\expandafter{\csname K:\the\count@\endcsname}%
		\else
		\toks@=\expandafter\expandafter\expandafter{%
			\expandafter\the\expandafter\toks@
			\expandafter;\expandafter\space
			\csname K:\the\count@\endcsname
		}%
		\fi
		\advance\count@ by 1 %
	}%
	\edef\x{\endgroup
		\noexpand\hypersetup{%
			pdfkeywords={\the\toks@}%
		}%
	}%
	\x
	\hypersetup{%
		pdfauthor={\@authname\ \@authsurn},
		pdftitle={\local@title},
		pdfsubject={\local@doctype\ de \@degreename\ em \local@deptname\ da COPPE/UFRJ},
		pdfcreator={LaTeX with CoppeTeX toolkit}
	}}
	\newcommand\makecatalog{%
		\vspace*{\fill}
		\begin{center}
			\setlength{\fboxsep}{5mm}
			\framebox[120mm][c]{\makebox[5mm][c]{}%
				\begin{minipage}[c]{105mm}
					\setlength{\parindent}{5mm}
					\noindent\sloppy\nohyphens\@authsurn,
					\nohyphens\@authname\par
					\nohyphens{\local@title/ \@authname\ \@authsurn. -- \local@cityname:
						UFRJ/Escola Politécnica, \number\year.}\par
					\pageref{front:pageno},
					\pageref{LastPage}
					p.\@ifundefined{r@cat:lofflag}{}{\pageref{cat:lofflag}} $29,7$cm.\par
					% There is an issue here. When the last entry must be split between lines,
					% the spacing between it and the next paragraph becomes smaller.
					% Should we manually introduce a fixed space? But how could we know that
					% a name was split?
					\begin{tabularx}{100mm}[b]{@{}l@{ }X@{}}
						\local@advisorstring: & \nohyphens{\@adname\ \@adsurn}%
						\ifthenelse{\equal{\@coadname}{\@empty}}{}{\\
							& \nohyphens{\@coadname\ \@coadsurn}}
					\end{tabularx}\par
					\nohyphens{\local@doctype\ de \@degreename\ --
						UFRJ/ Escola Politécnica/ Curso de \local@deptname, \number\year.}\par
					\bibname: p. 68 -- 70. \par
					%\pageref{bib:begin} -- \pageref{bib:end}.\par
					\count1=0
					\count2=1
					\nohyphens{\@whilenum \count1<\value{keywords} \do {%
							\number\count2. \csname K:\the\count1 \endcsname.
							\advance\count1 by 1
							\advance\count2 by 1}
						I. \@adsurn, \@adname%
						\ifthenelse{\equal{\@coadname}{\@empty}}{}{\emph{~et~al.}}.
						II. \local@universityname, UFRJ, Curso de \local@deptname.
						III. \local@title.}
				\end{minipage}}
			\end{center}
			\vspace*{\fill}}
		\newcommand\dedication[1]{
			\gdef\@dedic{#1}
			\chapter*{\vfill
				\begin{flushright}
					\begin{minipage}{60mm}
						\it \normalsize \@dedic
					\end{minipage}
				\end{flushright}}}
				
				\newenvironment{abstract}{%
					\clearpage
					\thispagestyle{plain}
					\abstract@toptext\par
					\vspace*{8.6mm}
					\begin{center}
						\sloppy\nohyphens{\MakeUppercase\local@title}\par
						\vspace*{13.2mm}
						\@authname\ \@authsurn \par
						\vspace*{7mm}
						\local@monthname/\number\year
					\end{center}\par
					\vspace*{\fill}
					\noindent%
					\begin{tabularx}{\textwidth}[b]{@{}l@{ }X@{}}
						\local@advisorstring: & \nohyphens{\@adname\ \@adsurn}\\
						\ifthenelse{\equal{\@coadname}{\@empty}}{}{%
							& \nohyphens{\@coadname\ \@coadsurn}\\}
					\end{tabularx}\par
					\vspace*{2mm}
					\noindent\local@deptstring: \local@deptname\par
					\vspace*{7mm}}{\vspace*{\fill}}
				\newenvironment{foreignabstract}{%
					\clearpage
					\thispagestyle{plain}
					\begin{otherlanguage}{english}
						\foreignabstract@toptext\par
						\vspace*{8.6mm}
						\begin{center}
							\sloppy\nohyphens{\MakeUppercase\foreign@title}\par
							\vspace*{13.2mm}
							\@authname\ \@authsurn \par
							\vspace*{7mm}
							\foreign@monthname/\number\year
						\end{center}\par
						\vspace*{\fill}
						\noindent%
						\begin{tabularx}{\textwidth}[b]{@{}l@{ }X@{}}
							\foreign@advisorstring: & \nohyphens{\@adname\ \@adsurn}\\
							\ifthenelse{\equal{\@coadname}{\@empty}}{}{%
								& \nohyphens{\@coadname\ \@coadsurn}\\}
						\end{tabularx}\par
						\vspace*{2mm}
						\noindent\foreign@deptstring: \foreign@deptname\par
						\vspace*{7mm}}{%
					\end{otherlanguage}
					\vspace*{\fill}
					\global\let\@author\@empty
					\global\let\@date\@empty
					\global\let\foreign@title\@empty
					\global\let\foreign@title\relax
					\global\let\local@title\@empty
					\global\let\local@title\relax
					\global\let\author\relax
					\global\let\author\relax
					\global\let\date\relax}
				\renewcommand\listoffigures{%
					\immediate\write\@auxout{%
						\string\newlabel{cat:lofflag}{{}{:~il.;}{}{page.\roman{page}}{}}}
					\if@twocolumn
					\@restonecoltrue\onecolumn
					\else
					\@restonecolfalse
					\fi
					\chapter*{\listfigurename}%
					\addcontentsline{toc}{chapter}{\listfigurename}%
					\@mkboth{\MakeUppercase\listfigurename}%
					{\MakeUppercase\listfigurename}%
					\@starttoc{lof}%
					\if@restonecol\twocolumn\fi
				}
				\renewcommand\listoftables{%
					\if@twocolumn
					\@restonecoltrue\onecolumn
					\else
					\@restonecolfalse
					\fi
					\chapter*{\listtablename}%
					\addcontentsline{toc}{chapter}{\listtablename}%
					\@mkboth{%
						\MakeUppercase\listtablename}%
					{\MakeUppercase\listtablename}%
					\@starttoc{lot}%
					\if@restonecol\twocolumn\fi
				}
				\newcommand\printlosymbols{%
					\renewcommand\glossaryname{\listsymbolname}%
					\@input@{\jobname.los}}
				\def\makelosymbols{%
					\newwrite\@losfile
					\immediate\openout\@losfile=\jobname.syx
					\def\symbl{\@bsphack\begingroup
						\@sanitize
						\@wrlos}\typeout
					{Writing index of symbols file \jobname.syx}%
					\let\makelosymbols\@empty
				}
				\@onlypreamble\makelosymbols
				\AtBeginDocument{%
					\@ifpackageloaded{hyperref}{%
						\def\@wrlos#1#2{%
							\protected@write\@losfile{}%
							{\string\indexentry{[#1] #2|hyperpage}{\thepage}}%
							\endgroup
							\@esphack}}{%
						\def\@wrlos#1#2{%
							\protected@write\@losfile{}%
							{\string\indexentry{[#1] #2}{\thepage}}%
							\endgroup
							\@esphack}}}
				\newcommand\printloabbreviations{%
					\renewcommand\glossaryname{\listabbreviationname}%
					\@input@{\jobname.lab}}
				\def\makeloabbreviations{%
					\newwrite\@labfile
					\immediate\openout\@labfile=\jobname.abx
					\def\abbrev{\@bsphack\begingroup
						\@sanitize
						\@wrlab}\typeout
					{Writing index of abbreviations file \jobname.abx}%
					\let\makeloabbreviations\@empty
				}
				\@onlypreamble\makeloabbreviations
				\AtBeginDocument{%
					\@ifpackageloaded{hyperref}{%
						\def\@wrlab#1#2{%
							\protected@write\@labfile{}%
							{\string\indexentry{[#1] #2|hyperpage}{\thepage}}%
							\endgroup
							\@esphack}}{%
						\def\@wrlab#1#2{%
							\protected@write\@labfile{}%
							{\string\indexentry{[#1] #2}{\arabic{page}}}%
							\endgroup
							\@esphack}}}
				\newdimen\bibindent%
				\setlength\bibindent{1.5em}%
				\renewenvironment{thebibliography}[1]%
				{\chapter*{\bibname}%
					\addcontentsline{toc}{chapter}{\bibname}%
					\immediate\write\@auxout{%
						\string\newlabel{bib:begin}{{}{\arabic{page}}{}{page.\arabic{page}}{}}}%
					\list{\@biblabel{\@arabic\c@enumiv}}%
					{\setlength{\labelwidth}{0ex}%
						\setlength{\leftmargin}{9.0ex}%
						\setlength{\itemindent}{-9.0ex}%
						\advance\leftmargin\labelsep%
						\@openbib@code%
						\usecounter{enumiv}%
						\let\p@enumiv\@empty%
						\renewcommand\theenumiv{\@arabic\c@enumiv}}%
					\sloppy%
					\clubpenalty4000%
					\@clubpenalty \clubpenalty%
					\widowpenalty4000%
					\sfcode`\.\@m}%
				{\def\@noitemerr%
					{\@latex@warning{Empty `thebibliography' environment}}%
					\immediate\write\@auxout{%
						\string\newlabel{bib:end}{{}{\arabic{page}}{}{page.\arabic{page}}{}}}%
					\endlist}
				\newenvironment{theglossary}{%
					\if@twocolumn%
					\@restonecoltrue\onecolumn%
					\else%
					\@restonecolfalse%
					\fi%
					\@mkboth{\MakeUppercase\glossaryname}%
					{\MakeUppercase\glossaryname}%
					\chapter*{\glossaryname}%
					\addcontentsline{toc}{chapter}{\glossaryname}
					\list{}
					{\setlength{\listparindent}{0in}%
						\setlength{\labelwidth}{1.0in}%
						\setlength{\leftmargin}{1.5in}%
						\setlength{\labelsep}{0.5in}%
						\setlength{\itemindent}{0in}}%
					\sloppy}%
				{\if@restonecol\twocolumn\fi%
					\endlist}
				\renewenvironment{theindex}{%
					\if@twocolumn
					\@restonecolfalse
					\else
					\@restonecoltrue
					\fi
					\twocolumn[\@makeschapterhead{\indexname}]%
					\@mkboth{\MakeUppercase\indexname}%
					{\MakeUppercase\indexname}%
					\thispagestyle{plain}\parindent\z@
					\addcontentsline{toc}{chapter}{\indexname}
					\parskip\z@ \@plus .3\p@\relax
					\columnseprule \z@
					\columnsep 35\p@
					\let\item\@idxitem}
				{\if@restonecol\onecolumn\else\clearpage\fi}
				\newcommand\glossaryname{Glossary}
				\newcommand\listabbreviationname{Lista de Abreviaturas}
				\newcommand\listsymbolname{Lista de Símbolos}
				\newcommand\local@advisorstring{Orientador}
				\newcommand\foreign@advisorstring{Advisor}
				\ifthenelse{\boolean{maledoc}}{%
					\newcommand\local@approvedname{Aprovado por}%
				}{%
				\newcommand\local@approvedname{Aprovada por}%
			}
			\newcommand\foreign@approvedname{Approved by}
			\newcommand\local@universityname{Universidade Federal do Rio de Janeiro}
			\newcommand\local@deptstring{Departamento}
			\newcommand\foreign@deptstring{Department}
			\newcommand\local@cityname{Rio de Janeiro}
			\newcommand\local@statename{RJ}
			\newcommand\local@countryname{Brasil}
			\newcommand\frontcover@maintext{
				\sloppy\nohyphens{\local@doctype\ de \@degreename\ apresentado ao Curso
					de \local@deptname\ da Escola Politécnica, \local@universityname,
					como parte dos requisitos necessários {\` a} obtenção do título de  \local@degname.}
			}
			\newcommand\frontpage@maintext{
				\noindent {\MakeUppercase\local@doctype} FINAL
				SUBMETIDO
				\sloppy\nohyphens{AO CORPO DOCENTE DO DEPARTAMENTO DE \MakeUppercase\local@deptname\
					DA ESCOLA POLITÉCNICA DA \MakeUppercase\local@universityname\ COMO
					PARTE DOS REQUISITOS NECESSÁRIOS PARA A OBTENÇÃO DO GRAU DE
					{\MakeUppercase\local@jobname. \par}}	
			}
			\newcommand\frontpage@bottomtext{%
				\begin{center}
					{\MakeUppercase{\local@cityname, \local@statename\ -- \local@countryname}}\par
					{\MakeUppercase\local@monthname\ DE \number\year}
				\end{center}%
			}
			\newcommand\abstract@toptext{%
				\noindent Resumo do Projeto de Graduação apresentado
				\sloppy\nohyphens{{\` a} Escola Politécnica/UFRJ como parte dos requisitos
					necessários para a obtenção do grau de
					\local@degname\ de Controle e Automação}
			}
			\newcommand\foreignabstract@toptext{%
				\noindent \sloppy\nohyphens{Abstract of \foreign@doctype\ presented to
					POLI/UFRJ as a partial fulfillment of the requirements for the
					degree of Control and Automation \foreign@degname\ }
			}

			%% 
			%%
			%% End of file `poli.cls'.
