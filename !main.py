#   - * -   c o d i n g :   c p 1 2 5 1   - * -  
 f r o m   q t p y . Q t C o r e   i m p o r t   *  
 f r o m   q t p y . Q t W i d g e t s   i m p o r t   *  
 f r o m   q t p y . Q t G u i   i m p o r t   *  
 f r o m   q t p y   i m p o r t   u i c  
 i m p o r t   s y s  
 i m p o r t   o s  
 f r o m   o d b c A c c e s s   i m p o r t   *  
 f r o m   m a t p l o t l i b . b a c k e n d s . b a c k e n d _ q t 5 a g g   i m p o r t   F i g u r e C a n v a s   a s   C a n v a s  
 f r o m   m a t p l o t l i b . b a c k e n d s . b a c k e n d _ q t 5 a g g   i m p o r t   N a v i g a t i o n T o o l b a r 2 Q T   a s   N a v T B  
 f r o m   m a t p l o t l i b . f i g u r e   i m p o r t   F i g u r e  
 f r o m   m y N a v i g a t i o n   i m p o r t   *  
 i m p o r t   i c o n s  
 i m p o r t   j s o n  
 f r o m   f u n c t o o l s   i m p o r t   p a r t i a l  
 i m p o r t   n u m p y   a s   n p  
 f r o m   s a v e T o D a t   i m p o r t   s a v e D A T  
 f r o m   d a t a _ s o u r c e _ l i b   i m p o r t   *  
 # i m p o r t   o s  
 # f r o m   s h u t i l   i m p o r t   c o p y f i l e  
 f r o m   r a y S e l e c t i o n D i a l o g   i m p o r t   *  
 i m p o r t   n u m p y . f f t   a s   f f t t  
 f r o m   r e p o r t L i b   i m p o r t   *  
 i m p o r t   x l w t  
  
 d e f   c o p y A c t i o n ( a c t i o n ) :  
         i f   n o t   a c t i o n . p a r e n t ( ) :  
                 p a r e n t = N o n e  
         e l s e :  
                 p a r e n t = a c t i o n . p a r e n t ( )  
         n e w A = Q A c t i o n ( p a r e n t )  
         n e w A . s e t I c o n ( a c t i o n . i c o n ( ) )  
         n e w A . s e t T e x t ( a c t i o n . t e x t ( ) )  
         n e w A . s e t C h e c k a b l e ( a c t i o n . i s C h e c k a b l e ( ) )  
         r e t u r n   n e w A  
  
 d e f   m o v i n g A v e r a g e ( d a t a , d e g r e e = 1 0 ) :      
         s m o o t h e d = n p . z e r o s ( l e n ( d a t a ) - d e g r e e + 1 )  
         f o r   i   i n   r a n g e ( l e n ( s m o o t h e d ) ) :  
                 s m o o t h e d [ i ] = s u m ( d a t a [ i : i + d e g r e e ] ) / d e g r e e  
         r e t u r n   s m o o t h e d  
  
 d e f   f f t _ f i l t e r ( m a x t i m e ,   d a t a ,   f r e q ) :  
         n u m p o i n t s   =   i n t ( n p . f l o o r ( f r e q * m a x t i m e ) )  
         y 1 = f f t t . r f f t ( d a t a )  
         i f   n u m p o i n t s   a n d   n u m p o i n t s < l e n ( d a t a ) :  
                 r e z   =   [ 0 ] * l e n ( y 1 )  
                 r e z [ 0 : n u m p o i n t s ] = y 1 [ 0 : n u m p o i n t s ]  
         r e t u r n   f f t t . i r f f t ( r e z )    
  
 c l a s s   M a t p l o t l i b W i d g e t ( C a n v a s ) :  
         d e f   _ _ i n i t _ _ ( s e l f ,   p a r e n t = N o n e ) :  
                 f i g u r e   =   F i g u r e ( f i g s i z e = ( 4 , 3 ) )  
                 s e l f . a x   =   f i g u r e . a d d _ s u b p l o t ( 1 1 1 )  
                 C a n v a s . _ _ i n i t _ _ ( s e l f ,   f i g u r e )  
                 c = C a n v a s ( F i g u r e ( ) )  
                 s e l f . s e t P a r e n t ( p a r e n t )  
                 C a n v a s . s e t S i z e P o l i c y ( s e l f ,   Q S i z e P o l i c y . E x p a n d i n g ,   Q S i z e P o l i c y . E x p a n d i n g )  
                 C a n v a s . u p d a t e G e o m e t r y ( s e l f )  
                 s e l f . f i g u r e = f i g u r e  
                 s e l f . a x . g r i d ( )  
                 s e l f . t b = N a v T B ( s e l f . f i g u r e . c a n v a s ,   s e l f )  
                 s e l f . t b . h i d e ( )  
                 s e l f . n a v   =   M y N a v i g a t i o n ( s e l f . a x ,   m p l w i d g e t = s e l f )  
 #                 s e l f . a x . s e t _ x l a b e l ( ' ^� �� W,   � � ' )  
                 s e l f . f i g u r e . s u b p l o t s _ a d j u s t ( r i g h t = 0 . 9 8 ,   t o p = 0 . 9 8 )  
  
 c l a s s   M y W i n d o w ( Q M a i n W i n d o w ) :  
 #         d e f   e v e n t F i l t e r ( s e l f ,   o b j ,   e v ) :  
 #                 i f   e v . t y p e ( ) = = Q E v e n t . K e y P r e s s :  
 #                         p r i n t ( e v . k e y ( ) )  
 #                         r e t u r n   T r u e  
 #                 r e t u r n   F a l s e  
         d e f   s c A c t i o n ( s e l f ,   d i r e c t i o n ) :  
                 i f   s e l f . t a b W i d g e t . c u r r e n t I n d e x ( ) ! = 3 :   r e t u r n  
                 l = s e l f . m p l P u l s e s . a x . g e t _ l i n e s ( )  
                 i f   l e n ( l ) < 4 :   r e t u r n  
                 d y = 1 e - 5  
                 m u l t = 1 . 0   i f   d i r e c t i o n = = ' u p '   e l s e   - 1 . 0  
                 l [ 2 ] . s e t _ y d a t a ( l [ 2 ] . g e t _ y d a t a ( ) + m u l t * s e l f . t r D y )  
                 s e l f . m p l P u l s e s . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
                  
         d e f   _ _ i n i t _ _ ( s e l f ,   p a r e n t = N o n e ) :  
                 s u p e r ( ) . _ _ i n i t _ _ ( p a r e n t )  
                 u i c . l o a d U i ( ' m a i n . u i ' ,   s e l f )  
                 s e l f . r a d i o B u t t o n s = [ ]  
                 f o r   g b   i n   [ s e l f . g b X ,   s e l f . g b Y 1 ,   s e l f . g b Y 2 ] :  
                         b 1   =   Q R a d i o B u t t o n ( " t " )  
                         b 2   =   Q R a d i o B u t t o n ( " e " )  
                         b 3   =   Q R a d i o B u t t o n ( " s " )  
                         b 4   =   Q R a d i o B u t t o n ( " d e " )  
                         g b . l a y o u t ( ) . a d d W i d g e t ( b 1 )  
                         g b . l a y o u t ( ) . a d d W i d g e t ( b 2 )  
                         g b . l a y o u t ( ) . a d d W i d g e t ( b 3 )  
                         g b . l a y o u t ( ) . a d d W i d g e t ( b 4 )  
                         s e l f . r a d i o B u t t o n s . a p p e n d ( [ b 1 ,   b 2 ,   b 3 ,   b 4 ] )  
                 s e l f . r a d i o B u t t o n s [ 0 ] [ 1 ] . s e t C h e c k e d ( T r u e )  
                 s e l f . r a d i o B u t t o n s [ 1 ] [ 2 ] . s e t C h e c k e d ( T r u e )  
                 s e l f . r a d i o B u t t o n s [ 2 ] [ 3 ] . s e t C h e c k e d ( T r u e )  
                 b   =   Q R a d i o B u t t o n ( " N o n e " )  
                 s e l f . g b Y 2 . l a y o u t ( ) . a d d W i d g e t ( b )  
                 s e l f . r a d i o B u t t o n s [ 2 ] . a p p e n d ( b )  
  
 #               M a t p l o t l i b   w i d g e t s  
                 s e l f . m p l O s c   =   M a t p l o t l i b W i d g e t ( s e l f )  
                 s e l f . m p l L a y o u t . a d d W i d g e t ( s e l f . m p l O s c )  
                 s e l f . m p l P u l s e s   =   M a t p l o t l i b W i d g e t ( s e l f )  
                 s e l f . v l P u l s e s . a d d W i d g e t ( s e l f . m p l P u l s e s )  
                 s e l f . m p l D i a g r a m m   =   M a t p l o t l i b W i d g e t ( s e l f )  
                 s e l f . v l D i a g r a m m . a d d W i d g e t ( s e l f . m p l D i a g r a m m )  
                 s e l f . m p l C o m p a r D i a g   =   M a t p l o t l i b W i d g e t ( s e l f )  
                 s e l f . v l C o m p a r D i a g . a d d W i d g e t ( s e l f . m p l C o m p a r D i a g )              
                 s e l f . m p l s = [ N o n e ,   s e l f . m p l O s c ,   N o n e ,   s e l f . m p l P u l s e s ,   s e l f . m p l D i a g r a m m ,   s e l f . m p l C o m p a r D i a g ]  
 #                 s e l f . t a b W i d g e t . i n s t a l l E v e n t F i l t e r ( s e l f )  
                 s e l f . s c U P = Q S h o r t c u t ( Q K e y S e q u e n c e ( ' C T R L + U P ' ) ,   s e l f )  
                 s e l f . s c D O W N = Q S h o r t c u t ( Q K e y S e q u e n c e ( ' C T R L + D O W N ' ) ,   s e l f )  
                 s e l f . s c U P . a c t i v a t e d . c o n n e c t ( p a r t i a l ( s e l f . s c A c t i o n ,   ' u p ' ) )  
                 s e l f . s c D O W N . a c t i v a t e d . c o n n e c t ( p a r t i a l ( s e l f . s c A c t i o n ,   ' d o w n ' ) )  
  
                 s e l f . t o o l B a r s = [ ]  
                 f o r   i   i n   r a n g e ( s e l f . t a b W i d g e t . c o u n t ( ) ) :  
                         s e l f . t o o l B a r s . a p p e n d ( s e l f . a d d T o o l B a r ( ' t b { } ' . f o r m a t ( i + 1 ) ) )  
                         s e l f . t o o l B a r s [ i ] . s e t V i s i b l e ( F a l s e )  
  
                 s e l f . t o o l B a r s [ 0 ] . a d d A c t i o n ( s e l f . a c t i o n S a v e T o D a t )  
                 s e l f . t o o l B a r s [ 0 ] . a d d A c t i o n ( s e l f . a c t i o n U p d a t e O D B C C o n t e n t )  
                 s e l f . t o o l B a r s [ 0 ] . s e t V i s i b l e ( T r u e )  
 #                 s e l f . t o o l B a r s [ 0 ] . a d d S e p a r a t o r ( )  
                 s e l f . t o o l B a r s [ 0 ] . a d d A c t i o n ( s e l f . a c t i o n R e a d D a t a )  
  
 # 	 O s c   t a b   t o o l   b a r   s e t u p  
  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n M p l H o m e )  
  
                 s e l f . o s c N a v M o d e A G = Q A c t i o n G r o u p ( s e l f . m p l O s c )  
                 s e l f . o s c N a v Z o o m M o d e = c o p y A c t i o n ( s e l f . a c t i o n Z o o m )  
                 s e l f . o s c N a v Z o o m M o d e . s e t D a t a ( ' z o o m ' )  
                 s e l f . o s c N a v M o d e A G . a d d A c t i o n ( s e l f . o s c N a v Z o o m M o d e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . o s c N a v Z o o m M o d e )  
  
                 s e l f . o s c N a v P a n M o d e = c o p y A c t i o n ( s e l f . a c t i o n P a n )  
                 s e l f . o s c N a v P a n M o d e . s e t D a t a ( ' p a n ' )  
                 s e l f . o s c N a v M o d e A G . a d d A c t i o n ( s e l f . o s c N a v P a n M o d e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . o s c N a v P a n M o d e )  
  
                 s e l f . o s c N a v I n t e r v a l M o d e = c o p y A c t i o n ( s e l f . a c t i o n I n t e r v a l )  
                 s e l f . o s c N a v I n t e r v a l M o d e . s e t D a t a ( ' i n t e r v a l ' )  
                 s e l f . o s c N a v M o d e A G . a d d A c t i o n ( s e l f . o s c N a v I n t e r v a l M o d e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . o s c N a v I n t e r v a l M o d e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d S e p a r a t o r ( )  
                 s e l f . o s c N a v M o d e A G . t r i g g e r e d . c o n n e c t ( s e l f . s e t M o d e )  
  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n C u t )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n Z e r o )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n S m o o t h )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n R e d u c e D a t a )  
 #                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n S c a l e R a y s )  
                 s e l f . t o o l B a r s [ 1 ] . a d d S e p a r a t o r ( )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n P l o t C u r v e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n P o l y F i t )  
                 s e l f . a c t i o n P l o t C u r v e . s e t P a r e n t ( s e l f . m p l O s c )  
                 s e l f . a c t i o n P l o t C u r v e . s e t D a t a ( ' c u r v e ' )  
                 s e l f . a c t i o n P l o t C u r v e . s e t C h e c k a b l e ( T r u e )  
                 s e l f . o s c N a v M o d e A G . a d d A c t i o n ( s e l f . a c t i o n P l o t C u r v e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n A p p l y C u r v e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n D e l e t e L i n e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n C o m p r e s s C u r v e )  
                 s e l f . t o o l B a r s [ 1 ] . a d d S e p a r a t o r ( )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n O p e n O S C )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . a c t i o n S a v e O S C )  
                 s e l f . g e t R a y F r o m E x p e r i m e n t = Q A c t i o n ( p a r e n t = s e l f ,   t e x t = ' G e t R a y ' )  
                 s e l f . t o o l B a r s [ 1 ] . a d d S e p a r a t o r ( )  
                 s e l f . t o o l B a r s [ 1 ] . a d d A c t i o n ( s e l f . g e t R a y F r o m E x p e r i m e n t )  
                 s e l f . g e t R a y F r o m E x p e r i m e n t . t r i g g e r e d . c o n n e c t ( s e l f . g e t R a y F r o m E x p e r i m e n t _ t r i g g e r e d )  
 #               t a b   1   e n d  
  
 #               t a b   3  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . a c t i o n M p l H o m e )  
  
                 s e l f . p l s s N a v M o d e A G = Q A c t i o n G r o u p ( s e l f . m p l P u l s e s )  
                 s e l f . p l s s N a v Z o o m M o d e = c o p y A c t i o n ( s e l f . a c t i o n Z o o m )  
                 s e l f . p l s s N a v Z o o m M o d e . s e t D a t a ( ' z o o m ' )  
                 s e l f . p l s s N a v M o d e A G . a d d A c t i o n ( s e l f . p l s s N a v Z o o m M o d e )  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . p l s s N a v Z o o m M o d e )  
  
                 s e l f . p l s s N a v P a n M o d e = c o p y A c t i o n ( s e l f . a c t i o n P a n )  
                 s e l f . p l s s N a v P a n M o d e . s e t D a t a ( ' p a n ' )  
                 s e l f . p l s s N a v M o d e A G . a d d A c t i o n ( s e l f . p l s s N a v P a n M o d e )  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . p l s s N a v P a n M o d e )  
  
                 s e l f . p l s s N a v I n t e r v a l M o d e = c o p y A c t i o n ( s e l f . a c t i o n I n t e r v a l )  
                 s e l f . p l s s N a v I n t e r v a l M o d e . s e t D a t a ( ' i n t e r v a l ' )  
                 s e l f . p l s s N a v M o d e A G . a d d A c t i o n ( s e l f . p l s s N a v I n t e r v a l M o d e )  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . p l s s N a v I n t e r v a l M o d e )  
                 s e l f . t o o l B a r s [ 3 ] . a d d S e p a r a t o r ( )  
                 s e l f . p l s s N a v M o d e A G . t r i g g e r e d . c o n n e c t ( s e l f . s e t M o d e )  
                 s e l f . t o o l B a r s [ 3 ] . a d d S e p a r a t o r ( )  
  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . a c t i o n C u t )  
                 s e l f . t o o l B a r s [ 3 ] . a d d S e p a r a t o r ( )  
  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . a c t i o n S a v e P u l s e s )  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . a c t i o n S y n c P u l s e s )  
  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . a c t i o n R e a d P u l s e s )  
                 s e l f . g e t P u l s e F r o m E x p e r i m e n t = Q A c t i o n ( p a r e n t = s e l f ,   t e x t = ' G e t P u l s e ' )  
                 s e l f . t o o l B a r s [ 3 ] . a d d S e p a r a t o r ( )  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . g e t P u l s e F r o m E x p e r i m e n t )  
                 s e l f . g e t P u l s e F r o m E x p e r i m e n t . t r i g g e r e d . c o n n e c t ( s e l f . g e t P u l s e F r o m E x p e r i m e n t _ t r i g g e r e d )  
                 s e l f . r e p a i r P u l s e = Q A c t i o n ( p a r e n t = s e l f ,   t e x t = ' r e p a i r P u l s e ' )  
                 s e l f . t o o l B a r s [ 3 ] . a d d A c t i o n ( s e l f . r e p a i r P u l s e )  
                 s e l f . r e p a i r P u l s e . t r i g g e r e d . c o n n e c t ( s e l f . r e p a i r P u l s e _ t r i g g e r e d )  
  
 #               t a b   3   e n d  
  
                 s e l f . t o o l B a r s [ 2 ] . a d d A c t i o n ( s e l f . a c t i o n S a v e E x p D a t a )  
  
                 s e l f . t o o l B a r s [ 4 ] . a d d A c t i o n ( s e l f . a c t i o n U p d a t e D i a g r a m m )  
                  
                 s e l f . c o r r E A c t i o n = Q A c t i o n ( t e x t = ' E c o r ' ,   p a r e n t = s e l f ,   i c o n = Q I c o n ( " : / i c o n s / u i / E c o r r " ) )  
                 s e l f . c o r r E A c t i o n . s e t C h e c k a b l e ( T r u e )  
                 s e l f . t o o l B a r s [ 5 ] . a d d A c t i o n ( s e l f . a c t i o n U p d a t e O D B C C o n t e n t )  
                 s e l f . t o o l B a r s [ 5 ] . a d d A c t i o n ( s e l f . c o r r E A c t i o n )  
                 s e l f . t o o l B a r s [ 5 ] . a d d S e p a r a t o r ( )  
                 s e l f . c h e c k A G = Q A c t i o n G r o u p ( s e l f )  
                 s e l f . c h e c k A G . a d d A c t i o n ( s e l f . a c t i o n C h e c k A l l )  
                 s e l f . c h e c k A G . a d d A c t i o n ( s e l f . a c t i o n C h e c k N o n e )  
                 s e l f . c h e c k A G . t r i g g e r e d . c o n n e c t ( s e l f . c h e c k A c t i o n )  
                 s e l f . t o o l B a r s [ 5 ] . a d d A c t i o n ( s e l f . a c t i o n C h e c k A l l )  
                 s e l f . t o o l B a r s [ 5 ] . a d d A c t i o n ( s e l f . a c t i o n C h e c k N o n e )  
  
                 s e l f . t o o l B a r s [ 5 ] . a d d S e p a r a t o r ( )  
                 s e l f . t o o l B a r s [ 5 ] . a d d A c t i o n ( s e l f . a c t i o n X L S e x p o r t )  
                 s e l f . t o o l B a r s [ 5 ] . a d d A c t i o n ( s e l f . a c t i o n C r e a t e R e p o r t )  
  
                 s e l f . t a b W i d g e t . c u r r e n t C h a n g e d . c o n n e c t ( s e l f . t a b C h a n g e d )  
                 s e l f . t b O p e n D a t a b a s e . s e t D e f a u l t A c t i o n ( s e l f . a c t i o n O p e n D a t a b a s e )  
                 s e l f . c b E x p T y p e . c u r r e n t I n d e x C h a n g e d . c o n n e c t ( s e l f . u p d a t e E x p N u m b e r s )  
                 s e l f . c b M a t e r i a l . c u r r e n t I n d e x C h a n g e d . c o n n e c t ( s e l f . u p d a t e E x p N u m b e r s )  
  
                 t r y :  
                         s e l f . c o n f = j s o n . l o a d ( o p e n ( ' c o n f . j s o n ' , ' r ' ) )  
                 e x c e p t :  
                         s e l f . c o n f = { }  
                 o d b c N a m e = s e l f . c o n f . g e t ( ' o d b c F n a m e ' ,   ' ' )  
                 s e l f . o d b c = N o n e  
                 i f   o d b c N a m e   a n d   o s . p a t h . e x i s t s ( o d b c N a m e ) :  
                         s e l f . l e D a t a b a s e F i l e . s e t T e x t ( s e l f . c o n f [ ' o d b c F n a m e ' ] )  
                         s e l f . o d b c = e x p O D B C ( s e l f . c o n f [ ' o d b c F n a m e ' ] )  
                         s e l f . u p d a t e O D B C c o n t e n t ( )  
  
                 s e l f . c o l o r s = [ ' r ' ,   ' b ' ,   ' g ' ]  
                 s e l f . e x p D a t a = [ ]  
                 s e l f . m p l D i a g r a m m . a x 2 = s e l f . m p l D i a g r a m m . a x . t w i n x ( )  
                 s e l f . m p l D i a g r a m m . f i g u r e . s u b p l o t s _ a d j u s t ( r i g h t = 0 . 9 ,   t o p = 0 . 9 8 )  
                 s e l f . l w E x p e r i m e n t s . i t e m C h a n g e d . c o n n e c t ( s e l f . l w E x p e r i m e n t s _ i t e m C h a n g e d )  
                 s e l f . m p l C o m p a r D i a g . a x 2 = s e l f . m p l C o m p a r D i a g . a x . t w i n x ( )  
                 s e l f . m p l C o m p a r D i a g . f i g u r e . s u b p l o t s _ a d j u s t ( r i g h t = 0 . 9 ,   t o p = 0 . 9 8 )  
                 s e l f . m p l C o m p a r D i a g . a x . l e g e n d ( )  
                 s e l f . c h a n n e l s = [ ]  
                 s e l f . t r D y = s e l f . c o n f . g e t ( ' t r D y ' ,   1 e - 4 )  
                 s e l f . s e t A c c e p t D r o p s ( T r u e )  
  
         d e f   d r a g E n t e r E v e n t ( s e l f ,   e ) :  
                 i f   e . m i m e D a t a ( ) . h a s U r l s ( ) :  
                         e . a c c e p t ( )  
                 e l s e :  
                         e . i g n o r e ( )  
          
         d e f   d r o p E v e n t ( s e l f ,   e ) :  
                 f o r   u   i n   e . m i m e D a t a ( ) . u r l s ( ) :  
                         p r i n t ( u . t o L o c a l F i l e ( ) )  
  
         d e f   p r i n t T o L o g ( s e l f ,   t e x t ) :  
                 s e l f . l L o g . a d d I t e m ( t e x t )  
  
         d e f   g e t A c t i v e C u r v e s ( s e l f ,   m p l = N o n e ) :  
                 c u r v e s = [ ]  
                 i f   n o t   m p l :  
                         m p l = s e l f . m p l s [ s e l f . t a b W i d g e t . c u r r e n t I n d e x ( ) ]  
                 l = m p l . a x . g e t _ l i n e s ( )  
                 f o r   i ,   c   i n   e n u m e r a t e ( s e l f . c h a n n e l s ) :  
                         i f   c . c h e c k S t a t e ( ) :  
                                 c u r v e s . a p p e n d ( l [ i ] )  
 #                 c u r v e s = l  
                 r e t u r n   c u r v e s  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n O p e n D a t a b a s e _ t r i g g e r e d ( s e l f ) :  
                 f n a m e = Q F i l e D i a l o g . g e t O p e n F i l e N a m e ( d i r e c t o r y = ' ' ,   f i l t e r = ' * . a c c d b ' ) [ 0 ]  
                 i f   f n a m e :  
                         s e l f . l e D a t a b a s e F i l e . s e t T e x t ( f n a m e )  
                         s e l f . o d b c = e x p O D B C ( f n a m e )  
                         s e l f . c o n f [ ' o d b c F n a m e ' ] = f n a m e  
                         s e l f . u p d a t e O D B C c o n t e n t ( )  
  
         d e f   u p d a t e O D B C c o n t e n t ( s e l f ) :  
                 i f   s e l f . o d b c :  
                         e x p T y p e s = s e l f . o d b c . g e t E x p T y p e s ( )  
                         s e l f . c b E x p T y p e . c l e a r ( )  
                         f o r   e t   i n   e x p T y p e s :  
                                 s e l f . c b E x p T y p e . a d d I t e m ( s t r ( e t [ '  \� �� � �� � ' ] ) + '   -   ' + s t r ( e t [ ' 	� � \� �� � �� � ' ] ) ,   e t )  
                         m a t e r i a l s = s e l f . o d b c . g e t M a t e r i a l s ( )  
                         s e l f . c b M a t e r i a l . c l e a r ( )  
                         f o r   m   i n   m a t e r i a l s :  
                                 s e l f . c b M a t e r i a l . a d d I t e m ( s t r ( m [ ' 
� �� � � ' ] ) + '   -   ' + s t r ( m [ ' 	� � 
� �� � � � ' ] ) ,   m )  
                         i d x s = s e l f . c o n f . g e t ( ' c u r r e n t E x p e r i m e n t ' ,   ( 0 , 0 , 0 ) )  
                         t r y :  
                                 s e l f . c b E x p T y p e . s e t C u r r e n t I n d e x ( i d x s [ 1 ] )  
                                 s e l f . c b M a t e r i a l . s e t C u r r e n t I n d e x ( i d x s [ 0 ] )  
                         e x c e p t :  
                                 p a s s  
                         s e l f . u p d a t e E x p N u m b e r s ( )              
                         s e l f . l w E x p e r i m e n t s . c l e a r ( )  
                         f o r   i   i n   r a n g e ( s e l f . c b E x p N u m b e r . c o u n t ( ) ) :  
 #                                 t = s e l f . c b E x p T y p e . i t e m D a t a ( s e l f . c b E x p T y p e . c u r r e n t I n d e x ( ) ) [ ' 	� � \� �� � �� � ' ]  
 #                                 m c = s e l f . c b M a t e r i a l . i t e m D a t a ( s e l f . c b M a t e r i a l . c u r r e n t I n d e x ( ) ) [ ' 	� � 
� �� � � � ' ]                                
 #                                 i t e m = Q L i s t W i d g e t I t e m ( s t r ( t ) + s t r ( m c ) + ' - ' + s e l f . c b E x p N u m b e r . i t e m T e x t ( i ) )  
                                 i t e m = Q L i s t W i d g e t I t e m ( s e l f . c b E x p N u m b e r . i t e m T e x t ( i ) )  
                                 # i t e m . s e t F l a g s ( Q t . I t e m I s U s e r C h e c k a b l e   a n d   Q t . I t e m I s E n a b l e d )  
                                 i t e m . s e t C h e c k S t a t e ( 0 )  
                                 s e l f . l w E x p e r i m e n t s . a d d I t e m ( i t e m )  
  
         d e f   u p d a t e E x p N u m b e r s ( s e l f ,   i d x = 0 ) :  
                 i f   n o t   s e l f . o d b c :  
                         r e t u r n  
                 t r y :  
                         t = s e l f . c b E x p T y p e . i t e m D a t a ( s e l f . c b E x p T y p e . c u r r e n t I n d e x ( ) ) [ ' 	� � \� �� � �� � ' ]  
                         m c = s e l f . c b M a t e r i a l . i t e m D a t a ( s e l f . c b M a t e r i a l . c u r r e n t I n d e x ( ) ) [ ' 	� � 
� �� � � � ' ]  
                 e x c e p t :  
                         r e t u r n  
                 n u m b e r s = s e l f . o d b c . g e t N u m b e r s ( t ,   m c )  
                 s e l f . c b E x p N u m b e r . c l e a r ( )  
                 n n = [ ]  
                 f o r   n   i n   n u m b e r s :  
                         t r y :  
                                 n n . a p p e n d ( n [ ' � � �� � � � � � ' ] )  
                         e x c e p t :  
                                 p a s s  
                 n n . s o r t ( )  
                 f o r   n   i n   n n :  
                         s e l f . c b E x p N u m b e r . a d d I t e m ( ' { } ' . f o r m a t ( n ) )  
                 i d x s = s e l f . c o n f . g e t ( ' c u r r e n t E x p e r i m e n t ' ,   ( 0 , 0 , 0 ) )  
                 s e l f . c b E x p N u m b e r . s e t C u r r e n t I n d e x ( i d x s [ 2 ] )  
  
         d e f   t a b C h a n g e d ( s e l f ,   t b ) :  
                 f o r   i   i n   r a n g e ( s e l f . t a b W i d g e t . c o u n t ( ) ) :  
                         s e l f . t o o l B a r s [ i ] . s e t V i s i b l e ( F a l s e )  
                 s e l f . t o o l B a r s [ t b ] . s e t V i s i b l e ( l e n ( s e l f . t o o l B a r s [ t b ] . a c t i o n s ( ) ) )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n R e a d D a t a _ t r i g g e r e d ( s e l f ) :  
                 f o r   m p l   i n   s e l f . m p l s :  
                         i f   m p l :  
                                 m p l . a x . c l e a r ( )  
                                 m p l . a x . g r i d ( )  
                                 m p l . n a v . i n t e r v a l = N o n e  
                                 m p l . n a v . m o d e = N o n e  
                 i f   s e l f . m p l O s c . n a v . c u r v e . l :   s e l f . m p l O s c . n a v . c u r v e . c l e a r ( )            
                 i f   n o t   s e l f . o d b c :  
                         r e t u r n  
                 t r y :  
                         t = s e l f . c b E x p T y p e . i t e m D a t a ( s e l f . c b E x p T y p e . c u r r e n t I n d e x ( ) ) [ ' 	� � \� �� � �� � ' ]  
                         m c = s e l f . c b M a t e r i a l . i t e m D a t a ( s e l f . c b M a t e r i a l . c u r r e n t I n d e x ( ) ) [ ' 	� � 
� �� � � � ' ]  
                         e n = s e l f . c b E x p N u m b e r . i t e m T e x t ( s e l f . c b E x p N u m b e r . c u r r e n t I n d e x ( ) )  
                         s e l f . c u r r e n t E x p C o d e = s t r ( t ) + s t r ( m c ) + ' - ' + e n  
                 e x c e p t :  
                         r e t u r n  
                 s e l f . e x p D a t a = s e l f . o d b c . g e t E x p e r i m e n t D a t a ( s e l f . c u r r e n t E x p C o d e )  
                 t r y :  
                         s e l f . s t r i c k e r D a t a = s e l f . o d b c . g e t S t r i c k e r D a t a ( s e l f . e x p D a t a [ '  � � � � ' ] )  
                 e x c e p t :  
                         s e l f . s t r i c k e r D a t a = { }  
                 s e l f . b a r D a t a = [ [ ] , [ ] ]  
                 t r y :  
                         s e l f . b a r D a t a [ 0 ] = s e l f . o d b c . g e t B a r D a t a ( s e l f . e x p D a t a [ ' � � V� � U!�  �� � �� X' ] )  
                         s e l f . b a r D a t a [ 1 ] = s e l f . o d b c . g e t B a r D a t a ( s e l f . e x p D a t a [ ' � � � � �  �� � �� X' ] )  
                 e x c e p t :  
                         s e l f . b a r D a t a = [ { } , { } ]  
                 i f   n o t   s e l f . e x p D a t a [ ' � � � � � � � � � � ' ] :  
                         s e l f . p r i n t T o L o g ( ' �  � � � � � � � � � � ' )  
                         r e t u r n  
                 t ,   r a y s = u n p a c k T a b l e ( s e l f . e x p D a t a [ ' � � � � � � � � � � ' ] )  
                 # s e l f . p r i n t T o L o g ( s t r ( l e n ( s e l f . c h a n n e l s ) ) )  
                 f o r   c   i n   s e l f . c h a n n e l s :  
                         s e l f . v l C h a n n e l s . r e m o v e W i d g e t ( c )  
                         c . c l o s e ( )  
                         d e l   c  
                 s e l f . c h a n n e l s = [ ]  
                 s e l f . v l C h a n n e l s . u p d a t e ( )  
                 f o r   i ,   r   i n   e n u m e r a t e ( r a y s ) :  
                         c b = Q C h e c k B o x ( s t r ( i + 1 ) ,   s e l f )  
                         s e l f . c h a n n e l s . a p p e n d ( c b )  
                         c b . s e t C h e c k e d ( T r u e )  
                         c b . s t a t e C h a n g e d . c o n n e c t ( s e l f . c b C h a n n e l C h e c k e d )  
                         s e l f . v l C h a n n e l s . a d d W i d g e t ( c b )  
                         c ,   =   s e l f . m p l O s c . a x . p l o t ( t * 1 e 6 ,   r ,   l a b e l = s t r ( i + 1 ) ,   c o l o r = s e l f . c o l o r s [ i ] )  
 #                         s e l f . c u r v e s . a p p e n d ( c )  
                 s e l f . m p l O s c . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
                 s e l f . p r i n t T o L o g ( '  � � � � �  � � � � � � ' )  
                 s e l f . c o n f [ ' c u r r e n t E x p e r i m e n t ' ] = ( s e l f . c b M a t e r i a l . c u r r e n t I n d e x ( ) ,   s e l f . c b E x p T y p e . c u r r e n t I n d e x ( ) ,  
                                                                                 s e l f . c b E x p N u m b e r . c u r r e n t I n d e x ( ) )  
                 s e l f . t S a m p l e . s e t I t e m ( 0 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a [ '  � � � ' ] ) ) )  
                 s e l f . t S a m p l e . s e t I t e m ( 1 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a [ '  � � �� ' ] ) ) )  
                 s e l f . t S a m p l e . s e t I t e m ( 2 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a [ ' � � � � � � W � � � ' ] ) ) )  
                 f o r   i ,   b   i n   e n u m e r a t e ( [ s e l f . t B a r 1 ,   s e l f . t B a r 2 ] ) :  
                         w = Q T a b l e W i d g e t I t e m ( s t r ( s e l f . b a r D a t a [ i ] . g e t ( '  � � � ( � � ) ' ,   0 ) ) )  
                         w . s e t F l a g s ( Q t . I t e m I s E d i t a b l e )  
                         b . s e t I t e m ( 0 , 0 ,   w )  
                         w = Q T a b l e W i d g e t I t e m ( s t r ( s e l f . b a r D a t a [ i ] . g e t ( '  � � �� ( � � ) ' , 0 ) ) )  
                         w . s e t F l a g s ( Q t . I t e m I s E d i t a b l e )  
                         b . s e t I t e m ( 4 , 0 ,   w )  
                         w = Q T a b l e W i d g e t I t e m ( s t r ( s e l f . b a r D a t a [ i ] . g e t ( ' 
� � V� X � V� � ( 
� ) ' , 0 ) ) )  
                         w . s e t F l a g s ( Q t . I t e m I s E d i t a b l e )  
                         b . s e t I t e m ( 3 , 0 ,   w )  
                         w = Q T a b l e W i d g e t I t e m ( s t r ( s e l f . b a r D a t a [ i ] . g e t ( '  � � � � X! ^V� ( � � �) ' , 0 ) ) )  
                         w . s e t F l a g s ( Q t . I t e m I s E d i t a b l e )  
                         b . s e t I t e m ( 2 , 0 ,   w )  
                         w = Q T a b l e W i d g e t I t e m ( s t r ( s e l f . b a r D a t a [ i ] . g e t ( ' 
� �� � � ' ,   ' ' ) ) )  
                         w . s e t F l a g s ( Q t . I t e m I s E d i t a b l e )  
                         b . s e t I t e m ( 6 , 0 ,   w )  
                 s e l f . t B a r 1 . s e t I t e m ( 1 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( ' � � � � �� � � � � ^ ( � � ) ' , 0 ) ) ) )  
                 s e l f . t B a r 2 . s e t I t e m ( 1 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( ' � � � � �� � � � � ^ ( � � ) ' , 0 ) ) ) )  
                 s e l f . t B a r 1 . s e t I t e m ( 5 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( ' 	� � � � ^� � � � � 	� ��� ��  ' , 0 ) ) ) )  
                 s e l f . t B a r 2 . s e t I t e m ( 5 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( ' 	� � � � ^� � � � � 	� ��� ��  ' , 0 ) ) ) )  
                 s e l f . t S t r i c k e r . s e t I t e m ( 0 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . s t r i c k e r D a t a . g e t ( '  � � �  � � � � � ( � � ) ' , 0 ) ) ) )  
                 s e l f . t S t r i c k e r . s e t I t e m ( 1 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . s t r i c k e r D a t a . g e t ( '  � � ��  � � � � � ( � � ) ' , 0 ) ) ) )  
                 s e l f . t S t r i c k e r . s e t I t e m ( 4 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . s t r i c k e r D a t a . g e t ( ' 
� �� � �  � � � � � ' , 0 ) ) ) )  
                 s e l f . t S t r i c k e r . s e t I t e m ( 2 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( '  � � � � X � � � � � ' , 0 ) ) ) )  
                 s e l f . t S t r i c k e r . s e t I t e m ( 3 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( '  � ^� �� �	  ' , 0 ) ) ) )  
                 s e l f . t E x p e r i m e n t . s e t I t e m ( 0 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( ' 	� � 
� �� � � � ' , 0 ) ) ) )  
                 s e l f . t E x p e r i m e n t . s e t I t e m ( 1 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( '  \� �� � �� � ' , 0 ) ) ) )  
                 s e l f . t E x p e r i m e n t . s e t I t e m ( 2 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( ' � � �� � � � � � ' , 0 ) ) ) )  
                 s e l f . t E x p e r i m e n t . s e t I t e m ( 3 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( '  �� �� � V� � ' , 2 0 ) ) ) )  
                 s e l f . t E x p e r i m e n t . s e t I t e m ( 4 , 0 ,   Q T a b l e W i d g e t I t e m ( s t r ( s e l f . e x p D a t a . g e t ( ' � � �� � � �' , ' ' ) ) ) )  
                 i f   s e l f . e x p D a t a [ ' � � V� X� � � � � � � � � �' ] :  
                         t ,   d   =   u n p a c k T a b l e ( s e l f . e x p D a t a [ ' � � V� X� � � � � � � � � �' ] )  
                         i f   l e n ( d ) > = 3 :  
                                 f o r   d d   i n   d [ : 3 ] :  
                                         i f   n p . m e a n ( d d ) < 0 :  
                                                 d d * = - 1 . 0  
                                         s e l f . m p l P u l s e s . a x . p l o t ( t * 1 e 6 ,   d d )  
                                 s e l f . t r D y = ( m a x ( d [ 2 ] ) - m i n ( d [ 2 ] ) ) / 1 0 0 .  
                                 s e l f . m p l P u l s e s . a x . p l o t ( t * 1 e 6 ,   d [ 0 ] - d [ 1 ] ,   ' k - - ' )  
                                 s e l f . m p l P u l s e s . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
                 s e l f . u p d a t e D i a g r a m m ( )  
  
         d e f   c l o s e E v e n t ( s e l f ,   e v e n t ) :  
                 i f   s e l f . o d b c :  
                         s e l f . o d b c . c l o s e ( )  
                         j s o n . d u m p ( s e l f . c o n f ,   o p e n ( ' c o n f . j s o n ' ,   ' w ' ) )  
  
         d e f   m p l R e d r a w ( s e l f ) :  
                 m p l = s e l f . m p l s [ s e l f . t a b W i d g e t . c u r r e n t I n d e x ( ) ]  
                 m p l . a x . s e t _ a u t o s c a l e x _ o n ( T r u e )  
                 m p l . a x . s e t _ a u t o s c a l e y _ o n ( T r u e )  
                 m p l . a x . r e l i m ( T r u e )  
                 m p l . a x . a u t o s c a l e _ v i e w ( )  
                 m p l . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
  
         d e f   s e t M o d e ( s e l f ,   a c t i o n ) :  
                 p r i n t ( a c t i o n )  
                 m p l = a c t i o n . a c t i o n G r o u p ( ) . p a r e n t ( )  
                 m o d e = a c t i o n . d a t a ( )  
                 m p l . n a v . m o d e = m o d e  
                 i f   m o d e   i n   [ ' i n t e r v a l ' ,   ' c u r v e ' ,   ' d i s t a n c e ' ] :  
                         i f   m p l . t b . _ a c t i v e = = ' Z O O M ' :  
                                 m p l . t b . z o o m ( )  
                         i f   m p l . t b . _ a c t i v e = = ' P A N ' :  
                                 m p l . t b . p a n ( )  
                 i f   m o d e = = ' z o o m '   a n d   m p l . t b . _ a c t i v e ! = ' Z O O M ' :  
                         m p l . t b . z o o m ( )  
                 i f   m o d e = = ' p a n '   a n d   m p l . t b . _ a c t i v e ! = ' P A N ' :  
                         m p l . t b . p a n ( )  
                 i f   m o d e = = " z o o m " :   m p l . s e t C u r s o r ( Q t . C r o s s C u r s o r )  
                 i f   m o d e = = " p a n " :   m p l . s e t C u r s o r ( Q t . O p e n H a n d C u r s o r )  
                 i f   m o d e = = " i n t e r v a l " :   m p l . s e t C u r s o r ( Q t . S i z e H o r C u r s o r )  
                 i f   m o d e = = " c u r v e " :   m p l . s e t C u r s o r ( Q t . C r o s s C u r s o r )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n M p l H o m e _ t r i g g e r e d ( s e l f ) :  
                 s e l f . m p l R e d r a w ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n C u t _ t r i g g e r e d ( s e l f ) :  
                 i i = s e l f . t a b W i d g e t . c u r r e n t I n d e x ( )  
                 m p l = s e l f . m p l s [ i i ]  
                 c u r v e s = m p l . a x . l i n e s  
                 i f   n o t   c u r v e s :   r e t u r n  
                 i f   n o t   ( m p l . n a v . i n t e r v a l ) :   r e t u r n  
                 x 1 ,   x 2   =   m p l . n a v . g e t _ i n t e r v a l ( )  
                 d t   =   x 2 - x 1  
                 r e z ,   o k   =   Q I n p u t D i a l o g . g e t D o u b l e ( s e l f ,   " C u t   i n t e r v a l " ,   " d t ,   m k s " ,   d t ,   0 ,   1 0 0 0 0 0 ,   5 )  
                 i f   n o t   o k :   r e t u r n  
                 x s   =   c u r v e s [ 0 ] . g e t _ x d a t a ( )  
                 n 1   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 1 )  
                 n 2   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 1 + r e z )  
                 x s = x s [ n 1 : n 2 ]  
                 x s = ( n p . a r r a y ( x s ) - x s [ 0 ] ) . t o l i s t ( )  
                 f o r   c   i n   c u r v e s :  
                         y = c . g e t _ y d a t a ( ) [ n 1 : n 2 ]  
                         c . s e t _ d a t a ( x s , y )  
                 m p l . n a v . r e m o v e _ i n t e r v a l ( )  
                 m p l . n a v . c u r v e . c l e a r ( )  
                 s e l f . m p l R e d r a w ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n Z e r o _ t r i g g e r e d ( s e l f ) :  
                 c u r v e s = s e l f . g e t A c t i v e C u r v e s ( )                
                 i f   n o t   ( s e l f . m p l O s c . n a v . i n t e r v a l ) :   r e t u r n  
                 x 1 ,   x 2   =   s e l f . m p l O s c . n a v . g e t _ i n t e r v a l ( )  
                 f o r   c   i n   c u r v e s :  
                         x s   =   c . g e t _ x d a t a ( )  
                         y s   =   c . g e t _ y d a t a ( )  
                         n 1   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 1 )  
                         n 2   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 2 )  
                         i f   n 1 = = n 2 :   r e t u r n  
                         y s - = n p . m e a n ( y s [ n 1 : n 2 ] )  
                         c . s e t _ d a t a ( x s , y s )  
                 s e l f . m p l R e d r a w ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n S m o o t h _ t r i g g e r e d ( s e l f ) :  
                 f l t r = s e l f . c o n f . g e t ( ' f i l t e r ' ,   0 )  
                 f l t r s = [ " F F T   f i l t e r " ,   " M o v i n g   a v e r a g e   s m o o t h i n g " ]  
                 i f   f l t r :  
                         f l t r s . r e v e r s e ( )  
                 t p ,   o k   =   Q I n p u t D i a l o g . g e t I t e m ( s e l f ,   " F i l t e r   t y p e " ,   " C h o o s e   a   t y p e   o f   f i l t e r " ,   f l t r s )  
                 i f   n o t   o k :   r e t u r n  
                 c u r v e s = s e l f . g e t A c t i v e C u r v e s ( )  
                 i f   l e n ( c u r v e s ) = = 0 :   r e t u r n  
                 i f   t p = = " F F T   f i l t e r " :  
                         s e l f . c o n f [ ' f i l t e r ' ] = 0  
                         r e z ,   o k   =   Q I n p u t D i a l o g . g e t I n t ( s e l f ,   " I n p u t   c u t   f r e q " ,   " f r e q ,   H z " ,   s e l f . c o n f . g e t ( ' f r e q C u t ' ,   1 0 0 0 0 0 ) ,   1 0 0 ,   1 0 0 0 0 0 0 0 ,   1 0 0 0 0 )  
                         i f   n o t   o k :   r e t u r n  
                         s e l f . c o n f [ ' f r e q C u t ' ] = r e z  
                         t m p _ c u r v e s = [ ]  
                         f o r   i ,   c   i n   e n u m e r a t e ( c u r v e s ) :                  
                                 x   =   c . g e t _ x d a t a ( )  
                                 y   =   c . g e t _ y d a t a ( )  
                                 m a x t = m a x ( x ) * 1 e - 6  
                                 y y   =   f f t _ f i l t e r ( m a x t ,   y ,   r e z )  
                                 y y   =   l i s t ( y y ) + [ y y [ - 1 ] ] * ( l e n ( x ) - l e n ( y y ) )  
                                 t m p _ c u r v e ,   =   s e l f . m p l O s c . a x . p l o t ( x , y y ,   [ " b l a c k " , " b r o w n " ] [ i ] )  
                                 t m p _ c u r v e s . a p p e n d ( t m p _ c u r v e )  
                                 s e l f . m p l R e d r a w ( )  
                 i f   t p = = " M o v i n g   a v e r a g e   s m o o t h i n g " :  
                         s e l f . c o n f [ ' f i l t e r ' ] = 1  
                         r e z ,   o k   =   Q I n p u t D i a l o g . g e t I n t ( s e l f ,   " I n p u t   w i n d o w   s i z e " ,   " P o i n t s " ,   s e l f . c o n f . g e t ( ' a v e P o i n t s ' ,   1 0 0 ) ,   2 ,   1 0 0 0 0 0 0 ,   5 0 )  
                         i f   n o t   o k :   r e t u r n  
                         s e l f . c o n f [ ' a v e P o i n t s ' ] = r e z  
                         t m p _ c u r v e s = [ ]  
                         f o r   i ,   c   i n   e n u m e r a t e ( c u r v e s ) :                  
                                 x   =   c . g e t _ x d a t a ( )  
                                 y   =   c . g e t _ y d a t a ( )  
                                 m a x t = m a x ( x ) * 1 e - 6  
                                 y y   =   m o v i n g A v e r a g e ( y ,   r e z )  
                                 y y   =   [ y y [ 0 ] ] * ( r e z / / 2 ) + l i s t ( y y ) + [ y y [ - 1 ] ] * ( l e n ( x ) - l e n ( y y ) - r e z / / 2 )  
                                 t m p _ c u r v e ,   =   s e l f . m p l O s c . a x . p l o t ( x , y y ,   [ " b l a c k " , " b r o w n " ] [ i ] )  
                                 t m p _ c u r v e s . a p p e n d ( t m p _ c u r v e )  
                                 s e l f . m p l R e d r a w ( )  
  
                 r e z   =   Q M e s s a g e B o x . q u e s t i o n ( s e l f ,   " A p p l y ? " ,   " A p p l y ? " ,   Q M e s s a g e B o x . Y e s   |   Q M e s s a g e B o x . N o )  
                 f o r   c , t m p   i n   z i p ( c u r v e s ,   t m p _ c u r v e s ) :    
                         i f   r e z   = =   Q M e s s a g e B o x . Y e s :  
                                 c . s e t _ d a t a ( x , t m p . g e t _ y d a t a ( ) )  
                         t m p . r e m o v e ( )  
                 s e l f . m p l R e d r a w ( )    
  
         d e f   c b C h a n n e l C h e c k e d ( s e l f ,   i d x ) :  
                 m p l = s e l f . m p l O s c  
                 l = m p l . a x . g e t _ l i n e s ( )  
                 f o r   i ,   c   i n   e n u m e r a t e ( s e l f . c h a n n e l s ) :  
                         l [ i ] . s e t _ v i s i b l e ( c . c h e c k S t a t e ( ) )  
                 s e l f . m p l R e d r a w ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n S a v e O S C _ t r i g g e r e d ( s e l f ) :  
                 c u r v e s = s e l f . g e t A c t i v e C u r v e s ( )  
                 i f   n o t   c u r v e s :   r e t u r n  
                 t = n p . a r r a y ( c u r v e s [ 0 ] . g e t _ x d a t a ( ) ) * 1 e - 6  
                 y = [ ]  
                 f o r   c   i n   c u r v e s :  
                         y . a p p e n d ( c . g e t _ y d a t a ( ) )  
                 o s c = p a c k T a b l e ( t , y )  
                 s e l f . o d b c . p u t O s c ( s e l f . c u r r e n t E x p C o d e ,   o s c )  
                 s e l f . e x p D a t a [ ' � � � � � � � � � � ' ] = o s c  
 #                 p r i n t ( s e l f . c u r r e n t E x p C o d e )  
                 s e l f . p r i n t T o L o g ( '  � � � � �  � � � � � � ' )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n S a v e E x p D a t a _ t r i g g e r e d ( s e l f ) :  
                 s e l f . e x p D a t a [ '  � � � ' ] = t o f l o a t ( s e l f . t S a m p l e . i t e m ( 0 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ '  � � �� ' ] = t o f l o a t ( s e l f . t S a m p l e . i t e m ( 1 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ ' � � � � � � W � � � ' ] = t o f l o a t ( s e l f . t S a m p l e . i t e m ( 2 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ] = t o f l o a t ( s e l f . t B a r 1 . i t e m ( 1 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ] = t o f l o a t ( s e l f . t B a r 2 . i t e m ( 1 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ] = t o f l o a t ( s e l f . t B a r 1 . i t e m ( 5 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ] = t o f l o a t ( s e l f . t B a r 2 . i t e m ( 5 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ '  � � � � X � � � � � ' ] = t o f l o a t ( s e l f . t S t r i c k e r . i t e m ( 2 , 0 ) . t e x t ( ) )  
                 s e l f . e x p D a t a [ ' � � �� � � �' ] = s t r ( s e l f . t E x p e r i m e n t . i t e m ( 4 , 0 ) . t e x t ( ) )  
                 s e l f . o d b c . p u t I n f o ( t a b l e = ' \� �� � �� ' ,  
                                                     p u t F i e l d s = ( '  � � � ' ,   '  � � �� ' ,   ' � � � � � � W � � � ' ,  
                                                                           ' � � � � �� � � � � ^ ( � � ) ' ,   ' � � � � �� � � � � ^ ( � � ) ' ,  
                                                                           ' 	� � � � ^� � � � � 	� ��� ��  ' ,   ' 	� � � � ^� � � � � 	� ��� ��  ' ,  
                                                                           '  � � � � X � � � � � ' ,   ' � � �� � � �' ) ,  
                                                     p u t F i e l d s V a l u e s = ( s e l f . e x p D a t a [ '  � � � ' ] ,   s e l f . e x p D a t a [ '  � � �� ' ] ,  
                                                                                       s e l f . e x p D a t a [ ' � � � � � � W � � � ' ] ,  
                                                                                       s e l f . e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ] ,   s e l f . e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ] ,  
                                                                                       s e l f . e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ] ,   s e l f . e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ] ,  
                                                                                       s e l f . e x p D a t a [ '  � � � � X � � � � � ' ] ,  
                                                                                       s e l f . e x p D a t a [ ' � � �� � � �' ] ) ,  
                                                     f i e l d s C o n d = ' 	� � � � � � � ' ,   f i e l d s C o n d V a l u e s = s e l f . c u r r e n t E x p C o d e )  
         @ S l o t ( )  
         d e f   o n _ a c t i o n R e a d P u l s e s _ t r i g g e r e d ( s e l f ) :  
                 i f   n o t   s e l f . e x p D a t a :   r e t u r n  
                 i f   n o t   s e l f . e x p D a t a . g e t ( ' � � � � � � � � � � ' ,   0 ) :   r e t u r n  
 #                 t , r s = u n p a c k T a b l e ( s e l f . e x p D a t a [ ' � � � � � � � � � � ' ] )  
                 c = s e l f . g e t A c t i v e C u r v e s ( m p l = s e l f . m p l O s c )  
                 i f   l e n ( c ) ! = 2 :  
                         s e l f . p r i n t T o L o g ( '  � � � � �   � X  ^� � � � �   2   � � � � � � � � � � � . ' )  
                         r e t u r n  
                 t = n p . a r r a y ( c [ 0 ] . g e t _ x d a t a ( ) )  
                 r s = [ c [ 0 ] . g e t _ y d a t a ( ) ,   c [ 1 ] . g e t _ y d a t a ( ) ]  
                 s c = 1   i f   s e l f . e x p D a t a [ '  \� �� � �� � ' ]   i n   [ ' t ' ,   ' u v ' ]   e l s e   - 1  
                 L d 1 = f l o a t ( s e l f . e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ] )  
                 c 1 = f l o a t ( s e l f . b a r D a t a [ 0 ] [ '  � � � � X! ^V� ( � � �) ' ] )  
                 L d 2 = f l o a t ( s e l f . e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ] )  
                 c 2 = f l o a t ( s e l f . b a r D a t a [ 1 ] [ '  � � � � X! ^V� ( � � �) ' ] )  
                 s e l f . m p l P u l s e s . a x . c l e a r ( )  
                 s e l f . m p l P u l s e s . a x . g r i d ( )  
                 t i n = t + L d 1 / c 1 * 1 0 0 0  
                 t r e f = t - L d 1 / c 1 * 1 0 0 0  
                 t t r = t - L d 2 / c 2 * 1 0 0 0  
                 d t = t i n [ 1 ] - t i n [ 0 ]  
                 N =   n p . c e i l ( ( t t r [ - 1 ] - t i n [ 0 ] ) / d t )  
                 t t = n p . l i n s p a c e ( t i n [ 0 ] ,   t t r [ - 1 ] ,   N )  
                 k 1 = t o f l o a t ( s e l f . e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ] )  
                 k 2 = t o f l o a t ( s e l f . e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ] )  
                 i n P = n p . i n t e r p ( t t ,   t i n ,   r s [ 0 ] * s c ) * k 1  
                 r e f P = n p . i n t e r p ( t t ,   t r e f ,   - r s [ 0 ] * s c ) * k 1  
                 t r P = n p . i n t e r p ( t t ,   t t r ,   r s [ 1 ] * s c ) * k 2  
                 s e l f . m p l P u l s e s . a x . p l o t ( t t ,   i n P )  
                 s e l f . m p l P u l s e s . a x . p l o t ( t t ,   r e f P )  
                 s e l f . m p l P u l s e s . a x . p l o t ( t t ,   t r P )  
                 s e l f . m p l P u l s e s . a x . p l o t ( t t ,   i n P - r e f P ,   ' k - - ' )  
                 s e l f . t r D y = ( m a x ( t r P ) - m i n ( t r P ) ) / 1 0 0 .  
                 s e l f . m p l R e d r a w ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n S a v e T o D a t _ t r i g g e r e d ( s e l f ) :  
                 i f   n o t   s e l f . e x p D a t a :   r e t u r n  
                 i f   n o t   s e l f . b a r D a t a :   r e t u r n  
                 f , o k   =   Q F i l e D i a l o g . g e t S a v e F i l e N a m e ( d i r e c t o r y = s e l f . c o n f . g e t ( ' l a s t D a t D i r ' , ' . ' )  
                                                                                       + o s . s e p + s e l f . c u r r e n t E x p C o d e ,   f i l t e r = ' * . d a t ' )  
                 i f   o k :  
                         s a v e D A T ( f ,   s e l f . e x p D a t a ,   s e l f . b a r D a t a )  
                         s e l f . c o n f [ ' l a s t D a t D i r ' ] = o s . p a t h . d i r n a m e ( o s . p a t h . a b s p a t h ( f ) )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n S a v e P u l s e s _ t r i g g e r e d ( s e l f ) :  
                 l = s e l f . m p l P u l s e s . a x . g e t _ l i n e s ( )  
                 i f   l e n ( l ) < 4 :   r e t u r n  
                 t = n p . a r r a y ( l [ 0 ] . g e t _ x d a t a ( ) ) * 1 e - 6  
                 y s = [ ]  
                 f o r   l l   i n   l [ : - 1 ] :  
                         y s . a p p e n d ( l l . g e t _ y d a t a ( ) )  
                 p = p a c k T a b l e ( t ,   y s )  
                 s e l f . o d b c . p u t P u l s e s ( s e l f . c u r r e n t E x p C o d e ,   p )  
  
         d e f   u p d a t e D i a g r a m m ( s e l f ) :  
                 l = s e l f . m p l P u l s e s . a x . g e t _ l i n e s ( )  
                 i f   l e n ( l ) < 4 :   r e t u r n  
                 s e l f . m p l D i a g r a m m . a x . c l e a r ( )  
                 s e l f . m p l D i a g r a m m . a x 2 . c l e a r ( )  
                 t ,   e t ,   s t ,   d e t = s e l f . c a l c u l a t e D i a g r a m ( s e l f . c u r r e n t E x p C o d e )  
                 d d e = m e a n D E ( { ' e t ' :   e t ,   ' s t ' :   s t ,   ' d e ' :   d e t } )  
                 s e l f . m p l D i a g r a m m . a x . p l o t ( e t , s t )  
                 s e l f . m p l D i a g r a m m . a x 2 . p l o t ( e t , d e t , ' r - - ' )  
                 p r i n t ( d d e )  
                 s e l f . m p l D i a g r a m m . a x 2 . a x h l i n e ( d d e ,   c o l o r = ' k ' ,   l s = ' - - ' )        
                 s e l f . m p l D i a g r a m m . a x 2 . t e x t ( 0 , d d e * 1 . 0 1 ,   ' { : . 1 f } ' . f o r m a t ( d d e ) )  
                 s e l f . m p l D i a g r a m m . a x . g r i d ( )  
                 s e l f . m p l D i a g r a m m . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
  
         d e f   c a l c u l a t e D i a g r a m ( s e l f ,   e x p C o d e ) :  
                 e x p D a t a = s e l f . o d b c . g e t E x p e r i m e n t D a t a ( e x p C o d e )  
                 i f   n o t   e x p D a t a [ ' � � V� X� � � � � � � � � �' ] :   r e t u r n  
                 t ,   y s = u n p a c k T a b l e ( e x p D a t a [ ' � � V� X� � � � � � � � � �' ] )  
                 y s = n p . a r r a y ( y s )  
                 f o r   i   i n   r a n g e ( l e n ( y s ) ) :  
                         i f   n p . m e a n ( y s [ i ] ) < 0 :  
                                 y s [ i ] * = - 1 . 0  
                 b 1 = s e l f . o d b c . g e t B a r D a t a ( e x p D a t a [ ' � � V� � U!�  �� � �� X' ] )  
                 b 2 = s e l f . o d b c . g e t B a r D a t a ( e x p D a t a [ ' � � � � �  �� � �� X' ] )  
                 c f g = { }  
                 c f g [ ' c 1 ' ] = t o f l o a t ( b 1 [ '  � � � � X! ^V� ( � � �) ' ] )  
                 c f g [ ' c 2 ' ] = t o f l o a t ( b 2 [ '  � � � � X! ^V� ( � � �) ' ] )  
                 c f g [ ' E 2 ' ] = t o f l o a t ( b 2 [ ' 
� � V� X � V� � ( 
� ) ' ] )  
                 D = t o f l o a t ( b 2 [ '  � � �� ( � � ) ' ] )  
                 D 0 = t o f l o a t ( b 2 [ '  � V� �� � �  � � �� ' ] )  
                 c f g [ ' S 2 ' ] = n p . p i * ( D * * 2 - D 0 * * 2 ) / 4 .  
                 c f g [ ' S s p ' ] = n p . p i * t o f l o a t ( e x p D a t a [ '  � � �� ' ] ) * * 2 / 4 .  
                 c f g [ ' L s p ' ] = t o f l o a t ( e x p D a t a [ '  � � � ' ] ) * 1 e - 3  
                 e t , s t , d e t = c a l c D i a g r a m ( t [ 1 ] - t [ 0 ] ,   [ y s [ 0 ] ] ,   [ y s [ 1 ] ] ,   [ y s [ 2 ] ] ,   c f g ,  
                                                             i s C o r r E = s e l f . c o r r E A c t i o n . i s C h e c k e d ( ) ,  
                                                             E c o r = s e l f . c o n f . g e t ( ' E c o r ' ,   1 0 0 0 0 0 . ) )  
                 r e t u r n   n p . a r r a y ( t ) * 1 e 6 ,   e t ,   s t ,   d e t  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n U p d a t e D i a g r a m m _ t r i g g e r e d ( s e l f ) :  
                 s e l f . u p d a t e D i a g r a m m ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n O p e n O S C _ t r i g g e r e d ( s e l f ) :  
                 i f   s e l f . m p l O s c . n a v . c u r v e . l :   s e l f . m p l O s c . n a v . c u r v e . c l e a r ( )                        
                 f n a m e = Q F i l e D i a l o g . g e t O p e n F i l e N a m e ( s e l f , " S e l e c t   F i l e " , s e l f . c o n f . g e t ( ' l a s t d i r ' , ' ' ) , " a l l ( * . l v m   * . l v z   * . n p z   * . t s v   * . d a t   * . c s v   * . t d m s   * . o s c ) ; ; \  
         l a b v i e w   f i l e s   ( * . l v m   * . l v z   * . t d m s ) ; ;   n p z - f i l e s   ( * . n p z ) ; ;   t x t - f i l e s   ( * . t x t ) ; ;   a g i l e n t   d a t a   ( * . t s v ) ; ;   d a t - f i l e   ( * . d a t ) ; ;   M i c r o s o f t   c s v   ( * . c s v ) ; ;   O c s i l o s c o p e   d a t a   ( * . o s c ) " )  
                 i f   f n a m e = = " " :   r e t u r n  
                 f n a m e = s t r ( f n a m e [ 0 ] )  
 #                 s e l f . a c t i o n  
                 s e l f . c o n f [ ' l a s t d i r ' ]   =   o s . p a t h . d i r n a m e ( f n a m e )  
                 i f   s e l f . m p l O s c . n a v . i n t e r v a l :   s e l f . m p l . n a v . r e m o v e _ i n t e r v a l ( )  
                 i f   f n a m e [ - 3 : ] . u p p e r ( ) = = ' L V M '   o r   f n a m e [ - 3 : ] . u p p e r ( ) = = ' L V Z '   :  
                         x , y 1 , y 2   =   l v m o p e n ( f n a m e )  
                 e l i f   f n a m e [ - 3 : ] . u p p e r ( ) = = ' N P Z ' :  
                         x , y 1 , y 2 = l o a d _ n p z ( f n a m e )  
                 e l i f   f n a m e [ - 3 : ] . u p p e r ( ) = = ' T X T ' :  
                         d a t a = n p . l o a d t x t ( f n a m e ,   u n p a c k = T r u e , s k i p r o w s = 2 )  
                         x = d a t a [ 0 ]  
                         y 1 = d a t a [ 1 ]  
                         y 2 = d a t a [ 2 ]  
                 e l i f   f n a m e [ - 3 : ] . u p p e r ( ) = = ' T S V ' :  
                         d a t a = n p . l o a d t x t ( f n a m e ,   u n p a c k = T r u e )  
                         x = d a t a [ 0 ]  
                         y 1 = d a t a [ 3 ]  
                         y 2 = d a t a [ 4 ]  
                 e l i f   f n a m e [ - 3 : ] . u p p e r ( ) = = ' D A T ' :  
                         d = d a t _ f i l e ( f n a m e )  
                         b y t e _ r a y s = d . b y t e _ r a y s  
                         y 1 = n p . a r r a y ( b y t e _ r a y s [ 0 ] ) * d . d i a p A  
                         y 2 = n p . a r r a y ( b y t e _ r a y s [ 1 ] ) * d . d i a p B  
                         x = n p . a r r a y ( l i s t ( r a n g e ( 1 0 2 4 ) ) ) * d . d t * 1 e - 6  
                 e l i f   f n a m e [ - 3 : ] . u p p e r ( ) = = ' C S V ' :  
                         d a t a = n p . l o a d t x t ( f n a m e ,   u n p a c k = T r u e , s k i p r o w s = 1 ,   d e l i m i t e r = ' , ' , u s e c o l s = ( 0 , 1 , 2 ) )  
                         x = d a t a [ 0 ]  
                         y 1 = d a t a [ 1 ]  
                         y 2 = d a t a [ 2 ]  
 #                 e l i f   f n a m e [ - 4 : ] . u p p e r ( ) = = ' T D M S ' :  
 #                         o b j e c t s ,   r a w d a t a = p y t d m s . r e a d ( f n a m e )  
 #                         x = r a w d a t a [ " / ' U n t i t l e d ' / ' T i m e ' " ]  
 #                         y 1 = r a w d a t a [ " / ' U n t i t l e d ' / ' U n t i t l e d   1 ' " ]  
 #                         y 2 = r a w d a t a [ " / ' U n t i t l e d ' / ' U n t i t l e d   2 ' " ]  
                 e l i f   f n a m e [ - 3 : ] . u p p e r ( ) = = ' O S C ' :  
                         c h a n n e l s = n p . l o a d ( f n a m e ) [ ' d a t a ' ]  
                         s e l f . c C o u n t = l e n ( c h a n n e l s )  
                         i f   l e n ( c h a n n e l s ) < 2 :  
                                 r e t u r n  
                         i d x 1 = 0  
                         i d x 2 = 1  
                         d t = c h a n n e l s [ 0 ] [ " d t " ]  
                         n = l e n ( c h a n n e l s [ 0 ] [ " d a t a " ] )  
                         x = n p . l i n s p a c e ( 0 , d t * n , n )  
                         i f   l e n ( c h a n n e l s ) > 2 :  
                                 d l g = r a y S e l e c t i o n D l g ( s e l f )  
                                 i f   n o t   d l g . e x e c _ ( ) :  
                                         r e t u r n  
                                 i d x 1 = d l g . c b R a y 1 . c u r r e n t I n d e x ( )  
                                 i d x 2 = d l g . c b R a y 2 . c u r r e n t I n d e x ( )  
                         s e l f . c o n f [ ' o s c R a y 1 ' ] = i d x 1  
                         s e l f . c o n f [ ' o s c R a y 2 ' ] = i d x 2  
                         y 1 = c h a n n e l s [ i d x 1 ] [ ' y 0 ' ] + c h a n n e l s [ i d x 1 ] [ ' d y ' ] * c h a n n e l s [ i d x 1 ] [ ' d a t a ' ]  
                         y 2 = c h a n n e l s [ i d x 2 ] [ ' y 0 ' ] + c h a n n e l s [ i d x 2 ] [ ' d y ' ] * c h a n n e l s [ i d x 2 ] [ ' d a t a ' ]  
                 e l s e :  
                         r e t u r n  
                 x   =   n p . a r r a y ( x ) * 1 e 6  
                 x - = x [ 0 ]  
                 s e l f . m p l O s c . a x . c l e a r ( )  
                 s e l f . m p l O s c . a x . g r i d ( )  
                 s e l f . m p l O s c . a x . p l o t ( x , y 1 )  
                 s e l f . m p l O s c . a x . p l o t ( x , y 2 )  
                 s e l f . m p l O s c . n a v . c u r v e . c l e a r ( )  
 #                 s e l f . m p l . a x . r e l i m ( )  
 #                 s e l f . m p l . a x . a u t o s c a l e ( )  
                 s e l f . m p l O s c . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n U p d a t e O D B C C o n t e n t _ t r i g g e r e d ( s e l f ) :  
                 c h e c k e d = [ ]  
                 f o r   i   i n   r a n g e ( s e l f . l w E x p e r i m e n t s . c o u n t ( ) ) :  
                         i i = s e l f . l w E x p e r i m e n t s . i t e m ( i )  
                         i f   i i . c h e c k S t a t e ( ) :                  
                                 c h e c k e d . a p p e n d ( i i . t e x t ( ) )  
                 s e l f . u p d a t e O D B C c o n t e n t ( )  
                 s e l f . m p l C o m p a r D i a g . a x . c l e a r ( )  
                 s e l f . m p l C o m p a r D i a g . a x 2 . c l e a r ( )  
                 s e l f . m p l C o m p a r D i a g . a x . g r i d ( )  
                 s e l f . m p l C o m p a r D i a g . a x . l e g e n d ( )  
                 s e l f . m p l C o m p a r D i a g . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
                 f o r   i   i n   r a n g e ( s e l f . l w E x p e r i m e n t s . c o u n t ( ) ) :  
                         i i = s e l f . l w E x p e r i m e n t s . i t e m ( i )  
                         i f   i i . t e x t ( )   i n   c h e c k e d :  
                                 i i . s e t C h e c k S t a t e ( 2 )  
  
         d e f   l w E x p e r i m e n t s _ i t e m C h a n g e d ( s e l f ,   i t e m ) :  
                 i f   n o t   i t e m . d a t a ( 1 0 0 ) :  
                         t = s e l f . c b E x p T y p e . i t e m D a t a ( s e l f . c b E x p T y p e . c u r r e n t I n d e x ( ) ) [ ' 	� � \� �� � �� � ' ]  
                         m c = s e l f . c b M a t e r i a l . i t e m D a t a ( s e l f . c b M a t e r i a l . c u r r e n t I n d e x ( ) ) [ ' 	� � 
� �� � � � ' ]                                
                         e x p C o d e = s t r ( t ) + s t r ( m c ) + ' - ' + i t e m . t e x t ( )  
                         t r y :  
                                 i d x s = [ 0 , 0 , 0 ]  
                                 f o r   i ,   r b g   i n   e n u m e r a t e ( s e l f . r a d i o B u t t o n s ) :  
                                         f o r   j ,   r b   i n   e n u m e r a t e ( r b g ) :  
                                                 i f   r b . i s C h e c k e d ( ) :  
                                                         i d x s [ i ]   =   j  
                                 p r i n t ( i d x s )  
                                 d a t a = s e l f . c a l c u l a t e D i a g r a m ( e x p C o d e )  
                                 l 1 , = s e l f . m p l C o m p a r D i a g . a x . p l o t ( d a t a [ i d x s [ 0 ] ] ,   d a t a [ i d x s [ 1 ] ] ,   l a b e l = e x p C o d e )  
                                 i f   i d x s [ 2 ] < 4 :  
                                         l 2 , = s e l f . m p l C o m p a r D i a g . a x 2 . p l o t ( d a t a [ i d x s [ 0 ] ] ,   d a t a [ i d x s [ 2 ] ] ,   ' - - ' ,   l w = 1 ,   c o l o r = l 1 . g e t _ c o l o r ( ) )  
                                 i t e m . s e t D a t a ( 1 0 0 ,   ( l 1 , l 2 ) )  
                         e x c e p t :  
                                 p a s s  
                 e l s e :  
                         i t e m . d a t a ( 1 0 0 ) [ 0 ] . s e t _ v i s i b l e ( i t e m . c h e c k S t a t e ( ) = = 2 )  
                         i t e m . d a t a ( 1 0 0 ) [ 1 ] . s e t _ v i s i b l e ( i t e m . c h e c k S t a t e ( ) = = 2 )  
                 s e l f . m p l C o m p a r D i a g . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
                 s e l f . m p l C o m p a r D i a g . a x . l e g e n d ( )  
                 s e l f . m p l C o m p a r D i a g . a x . l e g e n d ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n S y n c P u l s e s _ t r i g g e r e d ( s e l f ) :  
                 l = s e l f . m p l P u l s e s . a x . g e t _ l i n e s ( )  
                 p = [ l [ 0 ] . g e t _ x d a t a ( ) ,   [ l [ 0 ] . g e t _ y d a t a ( ) ,   l [ 1 ] . g e t _ y d a t a ( ) ,   l [ 2 ] . g e t _ y d a t a ( ) ] ]  
                 p p = s y n c P u l s e s ( p )  
                 l [ 0 ] . s e t _ y d a t a ( p p [ 1 ] [ 0 ] )  
                 l [ 1 ] . s e t _ y d a t a ( p p [ 1 ] [ 1 ] )  
                 l [ 2 ] . s e t _ y d a t a ( p p [ 1 ] [ 2 ] )  
                 l [ 3 ] . s e t _ y d a t a ( p p [ 1 ] [ 0 ] - p p [ 1 ] [ 1 ] )  
                 s e l f . m p l R e d r a w ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n R e d u c e D a t a _ t r i g g e r e d ( s e l f ) :  
                 l = s e l f . m p l O s c . a x . g e t _ l i n e s ( )  
                 i f   l e n ( l ) < 1 :   r e t u r n  
                 x s   =   n p . a r r a y ( l [ 0 ] . g e t _ x d a t a ( ) )  
                 r e z ,   o k   =   Q I n p u t D i a l o g . g e t I n t ( s e l f ,   " T h i n o u t   d e g r e e " ,   " C u r r e n t   n u m b e r   o f   p o i n t s   i s   % d .   D e v i d e   b y "   %   ( l e n ( x s ) , ) ,   1 0 ,   1 ,   1 0 0 0 0 0 0 ,   1 0 )  
                 i f   n o t   o k :   r e t u r n  
                 i f   r e z > = l e n ( x s ) :   r e t u r n  
                 f o r   l l   i n   l :  
                         y   =   l l . g e t _ y d a t a ( )  
                         l l . s e t _ x d a t a ( x s [ : : r e z ] )  
                         l l . s e t _ y d a t a ( y [ : : r e z ] )  
                 s e l f . m p l O s c . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
          
         @ S l o t ( )  
         d e f   o n _ a c t i o n A p p l y C u r v e _ t r i g g e r e d ( s e l f ) :  
                 i f   n o t   s e l f . m p l O s c . n a v . c u r v e . l :   r e t u r n  
                 c u r v e s = s e l f . g e t A c t i v e C u r v e s ( )  
                 i f   l e n ( c u r v e s ) = = 0 :   r e t u r n  
                 f o r   c   i n   c u r v e s :  
                         x s ,   y s   =   l i s t ( z i p ( * n p . s o r t ( n p . a r r a y ( s e l f . m p l O s c . n a v . c u r v e . p o i n t s , d t y p e = [ ( " x " , f l o a t ) , ( " y " , f l o a t ) ] ) , o r d e r = " x " ) ) )          
                         n 1 = n p . s e a r c h s o r t e d ( c . g e t _ x d a t a ( ) , x s [ 0 ] )  
                         n 2 = n p . s e a r c h s o r t e d ( c . g e t _ x d a t a ( ) , x s [ - 1 ] )  
                         x x = c . g e t _ x d a t a ( ) [ n 1 : n 2 ]  
                         y y = n p . i n t e r p ( x x , x s , y s )  
                         z z = c . g e t _ y d a t a ( )  
                         z z [ n 1 : n 2 ] = y y  
                         c . s e t _ y d a t a ( z z )  
                 s e l f . m p l O s c . n a v . c u r v e . c l e a r ( )  
                 s e l f . m p l O s c . f i g u r e . c a n v a s . d r a w _ i d l e ( )    
          
         @ S l o t ( )  
         d e f   o n _ a c t i o n D e l e t e L i n e _ t r i g g e r e d ( s e l f ) :  
                 i f   s e l f . m p l O s c . n a v . c u r v e . l :   s e l f . m p l O s c . n a v . c u r v e . c l e a r ( )    
                  
         @ S l o t ( )  
         d e f   o n _ a c t i o n C o m p r e s s C u r v e _ t r i g g e r e d ( s e l f ) :  
                 c u r v e s = s e l f . g e t A c t i v e C u r v e s ( )  
                 i f   s e l f . m p l O s c . n a v . i n t e r v a l :  
                         x 1 ,   x 2   =   s e l f . m p l O s c . n a v . g e t _ i n t e r v a l ( )  
                 e l i f   s e l f . m p l O s c . n a v . c u r v e . l :  
                                 x x = s e l f . m p l O s c . n a v . c u r v e . l . g e t _ x d a t a ( )  
                                 x 1 = m i n ( x x )  
                                 x 2 = m a x ( x x )  
                 e l s e :  
                         r e t u r n  
                 f o r   c   i n   c u r v e s :  
                         x s   =   c . g e t _ x d a t a ( )  
                         y s   =   c . g e t _ y d a t a ( )  
                         n 1   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 1 )  
                         n 2   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 2 )  
                         i f   n 1 = = n 2 :   r e t u r n  
                         x 1 = x s [ n 1 ]  
                         x 2 = x s [ n 2 ]  
                         y 1 = y s [ n 1 ]  
                         y 2 = y s [ n 2 ]  
                         i f   s e l f . m p l O s c . n a v . c u r v e . l :  
                                 x x s ,   y y s   =   l i s t ( z i p ( * n p . s o r t ( n p . a r r a y ( s e l f . m p l O s c . n a v . c u r v e . p o i n t s , d t y p e = [ ( " x " , f l o a t ) , ( " y " , f l o a t ) ] ) , o r d e r = " x " ) ) )          
                                 f = l a m b d a   x :   n p . i n t e r p ( x , x x s , y y s )                                  
                         e l s e :  
                                 f = l a m b d a   x :   ( x - x 1 ) / ( x 2 - x 1 ) * ( y 2 - y 1 ) + y 1  
                         s m a x = n p . a b s ( y s [ n 1 : n 2 ] - f ( n p . a r r a y ( x s [ n 1 : n 2 ] ) ) ) . m a x ( )  
                         p w r = 2 0  
 #                         i f   s e l f . a c t i o n E x p . i s C h e c k e d ( ) :  
 #                         g = l a m b d a   s :   1 . / n p . e x p ( n p . l o g ( 2 . ) * ( s / s m a x ) * * p w r )  
 #                         e l s e :  
                         g = l a m b d a   s :   0 . 5  
                         f o r   n   i n   r a n g e ( n 1 + 1 , n 2 ) :  
                                 s s = y s [ n ] - f ( x s [ n ] )  
                                 y s [ n ] = g ( n p . a b s ( s s ) ) * s s + f ( x s [ n ] )  
                         c . s e t _ d a t a ( x s , y s )  
                 s e l f . m p l O s c . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n P o l y F i t _ t r i g g e r e d ( s e l f ) :  
                 m ,   o k = Q I n p u t D i a l o g . g e t I n t ( s e l f , ' � � W� �   � � � � � � ' , ' m ' ,   v a l u e = 5 ,   m i n = 1 ,   m a x = 1 0 0 )  
                 c = s e l f . g e t A c t i v e C u r v e s ( )  
                 i f   t y p e ( c ) = = l i s t :  
                         c = c [ 0 ]  
                 i f   ( n o t   o k )   o r   ( n o t   s e l f . m p l O s c . n a v . i n t e r v a l )   o r   ( n o t   c ) :   r e t u r n  
                 x 1 ,   x 2   =   s e l f . m p l O s c . n a v . g e t _ i n t e r v a l ( )  
                 x s   =   c . g e t _ x d a t a ( )  
                 y s   =   c . g e t _ y d a t a ( )  
                 n 1   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 1 )  
                 n 2   =   n p . a r r a y ( x s ) . s e a r c h s o r t e d ( x 2 )  
                 i f   n 1 = = n 2 :   r e t u r n  
                 x s = x s [ n 1 : n 2 ]  
                 y s = y s [ n 1 : n 2 ]  
                 p = n p . p o l y f i t ( x s , y s , m )  
                 y s = n p . p o l y v a l ( p , x s )  
                 s e l f . m p l O s c . n a v . c u r v e . p o i n t s = l i s t ( z i p ( x s , y s ) )  
                 s e l f . m p l O s c . f i g u r e . c a n v a s . d r a w _ i d l e ( )  
          
         d e f   c h e c k A c t i o n ( s e l f ,   a c t ) :  
                 t o D o = a c t = = s e l f . a c t i o n C h e c k A l l  
                 f o r   i   i n   r a n g e ( s e l f . l w E x p e r i m e n t s . c o u n t ( ) ) :  
                         s e l f . l w E x p e r i m e n t s . i t e m ( i ) . s e t C h e c k S t a t e ( 2   i f   t o D o   e l s e   0 )  
                  
         @ S l o t ( )  
         d e f   o n _ a c t i o n X L S e x p o r t _ t r i g g e r e d ( s e l f ) :  
                 f = Q F i l e D i a l o g . g e t S a v e F i l e N a m e ( f i l t e r = ' * . x l s ' )  
                 i f   n o t   f :  
                         r e t u r n  
                 x l s = x l w t . W o r k b o o k ( )  
                 e x p P a r s = x l s . a d d _ s h e e t ( ' � � � � �� �   � � � � � ' )  
                 t = s e l f . c b E x p T y p e . i t e m D a t a ( s e l f . c b E x p T y p e . c u r r e n t I n d e x ( ) ) [ ' 	� � \� �� � �� � ' ]  
                 m c = s e l f . c b M a t e r i a l . i t e m D a t a ( s e l f . c b M a t e r i a l . c u r r e n t I n d e x ( ) ) [ ' 	� � 
� �� � � � ' ]                  
                 h e a d e r = [ ' 	� �   � � � � W' ,   '  � � �   V� � � � � ( � � ) ' ,   ' 
� �� � �   V� � � � � ' ,   '  � � � � X  V� � � � � ( � / c ) ' ,  
                                 '  �� �� � V� � ' ,   '  � � � � X  � ��� � � � � ' ,   '  � � � ( � � ) ' ,   '  � � �� ( � � ) ' ,   ' � � � � � � W  � � � � ( � � ) ' ,  
                                 ' � � � � �� � W  � ��� � � � � W( % ) ' ,   ' � � �� � � �' ,   '  � �   � � � � W' ]  
                 i f   t = = ' t ' :  
                         h e a d e r . i n s e r t ( - 3 ,   '  � � ��   Q�� ( � � ) ' )  
                         h e a d e r . i n s e r t ( - 3 ,   ' � �� �� X� � �  V� � � �� �( % ) ' )  
                         h e a d e r . i n s e r t ( - 3 ,   ' � �� �� X� � �  � V� �� �( % ) ' )  
                 f o r   i ,   h   i n   e n u m e r a t e ( h e a d e r ) :  
                         e x p P a r s . w r i t e ( 0 , i , h )  
                 r o w = 1  
                 N = s e l f . l w E x p e r i m e n t s . c o u n t ( )  
                 p r o g r e s s = Q P r o g r e s s D i a l o g ( )  
                 p r o g r e s s . s e t W i n d o w M o d a l i t y ( Q t . W i n d o w M o d a l )  
                 p r o g r e s s . s e t M a x i m u m ( N )  
                 p r o g r e s s . s e t M i n i m u m ( 0 )  
                 p r o g r e s s . s h o w ( )  
          
                 p r o g r e s s . s e t V a l u e ( 0 )                  
                 f o r   i   i n   r a n g e ( N ) :  
                         Q C o r e A p p l i c a t i o n . p r o c e s s E v e n t s ( )  
                         i f   p r o g r e s s . w a s C a n c e l e d ( ) :  
                                 b r e a k                          
                         i i = s e l f . l w E x p e r i m e n t s . i t e m ( i )  
                         i f   i i . c h e c k S t a t e ( ) :  
                                 e x p C o d e = s t r ( t ) + s t r ( m c ) + ' - ' + i i . t e x t ( )  
                                 r e p = s e l f . p r e p a r e R e p D a t a ( e x p C o d e )  
                                 e x p P a r s . w r i t e ( r o w , 0 , r e p [ ' e x p C o d e ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 1 , r e p [ ' s t r i k e r L ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 2 , r e p [ ' s t r i k e r M a t ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 3 , r e p [ ' s t r i k e r V ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 4 , r e p [ ' e x p T e m p ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 5 , r e p [ ' e x p D E ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 6 , r e p [ ' s a m p l e L ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 7 , r e p [ ' s a m p l e D ' ] )  
                                 e x p P a r s . w r i t e ( r o w , 8 , r e p [ ' s a m p l e L L ' ] )  
                                 i f   t = = ' t ' :  
                                         e x p P a r s . w r i t e ( r o w , 9 , r e p [ ' s a m p l e D D ' ] )  
                                         e x p P a r s . w r i t e ( r o w , 1 0 , r e p [ ' d e l t a ' ] )  
                                         e x p P a r s . w r i t e ( r o w , 1 1 , r e p [ ' k s i ' ] )  
                                 e x p P a r s . w r i t e ( r o w , h e a d e r . i n d e x ( ' � � � � �� � W  � ��� � � � � W( % ) ' ) ,   r e p . g e t ( ' e p ' , 0 ) )  
                                 e x p P a r s . w r i t e ( r o w , h e a d e r . i n d e x ( ' � � �� � � �' ) ,   r e p [ ' e x p R e m a r k ' ] )  
                                 e x p P a r s . w r i t e ( r o w , h e a d e r . i n d e x ( '  � �   � � � � W' ) ,   r e p [ ' e x p D a t e ' ] )  
                                 s h = x l s . a d d _ s h e e t ( e x p C o d e )  
                                 h 2 = [ ' ^� �� W( � � ) ' ,   ' � � � U!� ' ,   ' � � � � �� � � � ' ,   ' � � Q�� Q� ' ,   ' � � � U!� - � � � � �� � � � ' ,  
                                         ' � ��� � � � � W' ,   ' � � � W� �� �( 
� ) ' ,   ' � � � � � X  � ��� � � � � ( 1 / c ) ' ]  
                                 f o r   j ,   h   i n   e n u m e r a t e ( h 2 ) :  
                                         s h . w r i t e ( 0 , j , h )  
                                 p = r e p [ ' p u l s e s ' ]  
                                 d = r e p [ ' d i a g ' ]  
                                 r o w + = 1  
                                 p r o g r e s s . s e t V a l u e ( i )  
                                 i f   n o t   p   o r   n o t   d :  
                                         c o n t i n u e  
                                 f o r   j   i n   r a n g e ( l e n ( p [ 0 ] ) ) :  
                                         s h . w r i t e ( 1 + j , 0 ,   p [ 0 ] [ j ] * 1 e 6 )  
                                         s h . w r i t e ( 1 + j , 1 ,   p [ 1 ] [ 0 ] [ j ] )  
                                         s h . w r i t e ( 1 + j , 2 ,   p [ 1 ] [ 1 ] [ j ] )  
                                         s h . w r i t e ( 1 + j , 3 ,   p [ 1 ] [ 2 ] [ j ] )  
                                         s h . w r i t e ( 1 + j , 4 ,   p [ 1 ] [ 0 ] [ i ] - p [ 1 ] [ 1 ] [ j ] )  
                                         s h . w r i t e ( 1 + j , 5 ,   d [ 0 ] [ j ] )  
                                         s h . w r i t e ( 1 + j , 6 ,   d [ 1 ] [ j ] )  
                                         s h . w r i t e ( 1 + j , 7 ,   d [ 2 ] [ j ] )                          
                 x l s . s a v e ( f [ 0 ] )  
                 p r o g r e s s . c l o s e ( )  
  
         @ S l o t ( )  
         d e f   o n _ a c t i o n C r e a t e R e p o r t _ t r i g g e r e d ( s e l f ) :  
                 d r   =   Q F i l e D i a l o g . g e t E x i s t i n g D i r e c t o r y ( )  
                 i f   n o t   d r :  
                         r e t u r n  
                 t = s e l f . c b E x p T y p e . i t e m D a t a ( s e l f . c b E x p T y p e . c u r r e n t I n d e x ( ) ) [ ' 	� � \� �� � �� � ' ]  
                 m c = s e l f . c b M a t e r i a l . i t e m D a t a ( s e l f . c b M a t e r i a l . c u r r e n t I n d e x ( ) ) [ ' 	� � 
� �� � � � ' ]    
                 N = s e l f . l w E x p e r i m e n t s . c o u n t ( )  
                 p r o g r e s s = Q P r o g r e s s D i a l o g ( )  
                 p r o g r e s s . s e t W i n d o w M o d a l i t y ( Q t . W i n d o w M o d a l )  
                 p r o g r e s s . s e t M a x i m u m ( N )  
                 p r o g r e s s . s e t M i n i m u m ( 0 )  
                 p r o g r e s s . s h o w ( )  
                  
                 p r o g r e s s . s e t V a l u e ( 0 )  
                 f o r   i   i n   r a n g e ( N ) :  
                         Q C o r e A p p l i c a t i o n . p r o c e s s E v e n t s ( )  
                         i f   p r o g r e s s . w a s C a n c e l e d ( ) :  
                                 b r e a k  
                         i i = s e l f . l w E x p e r i m e n t s . i t e m ( i )  
                         i f   i i . c h e c k S t a t e ( ) :  
                                 e x p C o d e = s t r ( t ) + s t r ( m c ) + ' - ' + i i . t e x t ( )  
                                 r e p = s e l f . p r e p a r e R e p D a t a ( e x p C o d e )  
                                 c r e a t e R e p o r t ( r e p ,   d r )  
                         p r o g r e s s . s e t V a l u e ( i )  
 #                         p r o g r e s s . u p d a t e ( )  
                 p r o g r e s s . c l o s e ( )  
                  
         d e f   p r e p a r e R e p D a t a ( s e l f ,   e x p C o d e ) :  
                 r e p = { }  
                 r e p [ ' e x p C o d e ' ] = e x p C o d e  
                 e x p D a t a = s e l f . o d b c . g e t E x p e r i m e n t D a t a ( e x p C o d e )  
                 b 1 = s e l f . o d b c . g e t B a r D a t a ( e x p D a t a [ ' � � V� � U!�  �� � �� X' ] )  
                 b 2 = s e l f . o d b c . g e t B a r D a t a ( e x p D a t a [ ' � � � � �  �� � �� X' ] )  
                 s t = s e l f . o d b c . g e t S t r i c k e r D a t a ( e x p D a t a [ '  � � � � ' ] )  
                 m = s e l f . o d b c . g e t I n f o ( ' 
� �� � � \� �� � �� ' , ' 	� � 
� �� � � � ' ,   e x p D a t a [ ' 	� � 
� �� � � � ' ] ) [ 0 ]  
                 e t y p e = s e l f . o d b c . g e t I n f o ( '  \� �� � �� � ' ,   ' 	� � \� �� � �� � ' ,   e x p D a t a [ '  \� �� � �� � ' ] ) [ 0 ]  
                 t r y :  
                         r e p [ ' d i a g ' ] = s e l f . c a l c u l a t e D i a g r a m ( e x p C o d e ) [ 1 : ]  
                 e x c e p t :  
                         r e p [ ' d i a g ' ] = [ ]  
                 t ,   y s = u n p a c k T a b l e ( e x p D a t a [ ' � � V� X� � � � � � � � � �' ] )  
                 y s = n p . a r r a y ( y s )  
                 f o r   i   i n   r a n g e ( l e n ( y s ) ) :  
                         i f   n p . m e a n ( y s [ i ] ) < 0 :  
                                 y s [ i ] * = - 1 . 0  
                 r e p [ ' p u l s e s ' ] = [ t ,   y s ]  
                 r e p [ ' e x p D a t e ' ] = ' ' # s t r ( e x p D a t a [ '  � � ' ] ) . s p l i t ( ) [ 0 ]  
                 r e p [ ' e x p T i m e ' ] = ' '  
                 r e p [ ' e x p T e m p ' ] = f l o a t ( e x p D a t a [ '  �� �� � V� � ' ] )  
                 r e p [ ' e x p R e m a r k ' ] = s t r ( e x p D a t a [ ' � � �� � � �' ] )  
                 i f   r e p [ ' e x p R e m a r k ' ] = = ' N o n e ' :  
                         r e p [ ' e x p R e m a r k ' ] = ' '  
                 r e p [ ' s t r i k e r V ' ] = f l o a t ( e x p D a t a [ '  � � � � X � � � � � ' ] )  
                 r e p [ ' s a m p l e L ' ] = f l o a t ( e x p D a t a [ '  � � � ' ] )  
                 r e p [ " s t r i k e r L " ] = f l o a t ( s t [ '  � � �  � � � � � ( � � ) ' ] )  
                 r e p [ " s t r i k e r M a t " ] = s t r ( s t [ ' 
� �� � �  � � � � � ' ] )  
                 r e p [ ' s a m p l e D ' ] = f l o a t ( e x p D a t a [ '  � � �� ' ] )  
                 r e p [ ' s a m p l e S ' ] = n p . p i * f l o a t ( e x p D a t a [ '  � � �� ' ] ) * * 2 / 4 . 0  
                 t r y :  
                         p r i n t ( e x p C o d e )  
                         r e p [ ' e x p D E ' ] = m e a n D E ( d i c t ( z i p ( [ ' e t ' ,   ' s t ' ,   ' d e ' ] ,   r e p [ ' d i a g ' ] ) ) )  
                 e x c e p t :  
                         p r i n t ( ' C a n t   c a l c u l a t e   m e a n D E ' )  
                         r e p [ ' e x p D E ' ] = f l o a t ( e x p D a t a [ '  � � � � X ��� � � � � ' ] )  
                 r e p [ ' s a m p l e L L ' ] = L L = f l o a t ( e x p D a t a [ ' � � � � � � W � � � ' ] )  
                 i f   r e p [ ' e x p C o d e ' ] [ 0 ] = = ' c ' :  
                         r e p [ ' e p ' ] = a b s ( n p . l o g ( L L / r e p [ ' s a m p l e L ' ] ) ) * 1 0 0   i f   L L   a n d   r e p [ ' s a m p l e L ' ]   e l s e   0  
                 e l i f   r e p [ ' e x p C o d e ' ] [ 0 ] = = ' t ' :  
                         r e p [ ' s a m p l e D D ' ] = D D = f l o a t ( e x p D a t a [ '   �� � ' ] )  
                         D = f l o a t ( e x p D a t a [ '  � � �� ' ] )  
                         L = f l o a t ( e x p D a t a [ '  � � � ' ] )  
                         r e p [ ' d e l t a ' ] = ( L L - L ) / L * 1 0 0  
                         r e p [ ' k s i ' ] = ( D * * 2 - D D * * 2 ) / D * * 2 * 1 0 0   i f   D   e l s e   0  
                         r e p [ ' e p ' ] = 2 * n p . l o g ( D / D D ) * 1 0 0   i f   D D   e l s e   0  
                  
                 r e p [ ' m a t N a m e ' ] = m [ ' 
� �� � � ' ]  
                 r e p [ ' m a t C o n d i t i o n ' ] = ' � � � ^� '  
                 r e p [ ' e x p T y p e ' ] = e t y p e [ '  \� �� � �� � ' ]  
                 r e p [ " e x p S e t u p " ] = " R S- { } " . f o r m a t ( b 1 [ '  � � �� ( � � ) ' ] )  
                 r e p [ " e x p C h i e f " ] = e x p D a t a [ ' ^�� ^�� � � � ! � � � � � � W' ]  
                 r e p [ " r o o m T e m p " ] = e x p D a t a [ '  �� �� � V� � � � �!�� W' ]  
                 r e p [ " r o o m W e t n e s s " ] = e x p D a t a [ '  � � � � � � X' ]  
                 r e p [ " s a m p l e R e m a r k " ] = " "  
                 r e p [ " b a r 1 M a t " ] = b 1 [ ' 
� �� � � ' ]  
                 r e p [ " b a r 2 M a t " ] = b 2 [ ' 
� �� � � ' ]  
                 r e p [ " b a r 1 S " ] = f l o a t ( b 1 [ '  � � �� ( � � ) ' ] ) * * 2 * 3 . 1 4 / 4 .  
                 r e p [ " b a r 2 S " ] = f l o a t ( b 2 [ '  � � �� ( � � ) ' ] ) * * 2 * 3 . 1 4 / 4 .  
                 r e p [ " b a r 1 E " ] = b 1 [ ' 
� � V� X � V� � ( 
� ) ' ]  
                 r e p [ " b a r 2 E " ] = b 2 [ ' 
� � V� X � V� � ( 
� ) ' ]  
                 r e p [ " b a r 1 C " ] = f l o a t ( b 1 [ '  � � � � X! ^V� ( � � �) ' ] )  
                 r e p [ " b a r 2 C " ] = f l o a t ( b 2 [ '  � � � � X! ^V� ( � � �) ' ] )  
                 r e p [ " b a r 1 K " ] = e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ]  
                 r e p [ " b a r 2 K " ] = e x p D a t a [ ' 	� � � � ^� � � � � 	� ��� ��  ' ]  
                 r e p [ " b a r 1 L " ] = b 1 [ '  � � � ( � � ) ' ]  
                 r e p [ " b a r 2 L " ] = b 2 [ '  � � � ( � � ) ' ]  
                 r e p [ " g a u g e 1 P o s i t i o n " ] = e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ]  
                 r e p [ " g a u g e 2 P o s i t i o n " ] = e x p D a t a [ ' � � � � �� � � � � ^ ( � � ) ' ]  
                 r e p [ " b a r s R e m a r k " ] = " "  
                 r e p [ " s t r i k e r D " ] = s t [ '  � � ��  � � � � � ( � � ) ' ]  
                 r e p [ " l o g o I m g " ] = " l o g o 2 . j p g "  
                 r e p [ " s y n c I m g " ] = " "  
                 r e p [ " d i a g r I m g " ] = " "  
                 r e p [ " t a b l e L i n e s " ] = ' '  
                 r e p [ " e x p A d d i t i o n a l C e l l s " ] = " "                  
                 r e t u r n   r e p  
          
         d e f   g e t R a y F r o m E x p e r i m e n t _ t r i g g e r e d ( s e l f ) :  
                 l = [ ]  
                 f o r   i   i n   r a n g e ( s e l f . c b E x p N u m b e r . c o u n t ( ) ) :  
                         l . a p p e n d ( s e l f . c b E x p N u m b e r . i t e m T e x t ( i ) )  
                 i d x ,   o k = Q I n p u t D i a l o g . g e t I t e m ( s e l f ,   " C h o o s e   e x p e r i m e n t   i n d e x " ,  
                                                                   " e x p e r i m e n t   i n d e x " ,   l ,   e d i t a b l e = F a l s e )  
                 i f   o k :  
                         r = s e l f . o d b c . g e t E x p e r i m e n t D a t a ( s e l f . c u r r e n t E x p C o d e . s p l i t ( ' - ' ) [ 0 ] + ' - ' + i d x ) [ ' � � � � � � � � � � ' ]  
                         t , r r = u n p a c k T a b l e ( r )  
                         l = s e l f . m p l O s c . a x . g e t _ l i n e s ( )  
                         n e w Y Y = n p . i n t e r p ( l [ 0 ] . g e t _ x d a t a ( ) ,   n p . a r r a y ( t ) * 1 e 6 ,   r r [ 0 ] )  
                         l [ 0 ] . s e t _ y d a t a ( n e w Y Y )  
                         s e l f . m p l R e d r a w ( )  
                          
         d e f   g e t P u l s e F r o m E x p e r i m e n t _ t r i g g e r e d ( s e l f ) :  
                 l = [ ]  
                 f o r   i   i n   r a n g e ( s e l f . c b E x p N u m b e r . c o u n t ( ) ) :  
                         l . a p p e n d ( s e l f . c b E x p N u m b e r . i t e m T e x t ( i ) )  
                 i d x ,   o k = Q I n p u t D i a l o g . g e t I t e m ( s e l f ,   " C h o o s e   e x p e r i m e n t   i n d e x " ,  
                                                                   " e x p e r i m e n t   i n d e x " ,   l ,   e d i t a b l e = F a l s e )  
                 i f   o k :  
                         r = s e l f . o d b c . g e t E x p e r i m e n t D a t a ( s e l f . c u r r e n t E x p C o d e . s p l i t ( ' - ' ) [ 0 ] + ' - ' + i d x ) [ ' � � V� X� � � � � � � � � �' ]  
                         t , r r = u n p a c k T a b l e ( r )  
                         i d x 2 ,   o k = Q I n p u t D i a l o g . g e t I t e m ( s e l f ,   " C h o o s e   p u l s e   i n d e x " ,  
                                                                                     " p u l s e   i n d e x " ,   [ ' 1 ' ,   ' 2 ' ,   ' 3 ' ] ,  
                                                                                     e d i t a b l e = F a l s e )  
                         i f   o k :  
                                 l = s e l f . m p l P u l s e s . a x . g e t _ l i n e s ( )  
                                 i = i n t ( i d x 2 ) - 1  
                                 n e w Y Y = n p . i n t e r p ( l [ i ] . g e t _ x d a t a ( ) ,   n p . a r r a y ( t ) * 1 e 6 ,   r r [ i ] )  
                                 l [ i ] . s e t _ y d a t a ( n e w Y Y )  
                                 s e l f . m p l R e d r a w ( )  
  
         d e f   r e p a i r P u l s e _ t r i g g e r e d ( s e l f ) :  
                 i d x ,   o k = Q I n p u t D i a l o g . g e t I t e m ( s e l f ,   " C h o o s e   p u l s e   t o   r e p a i r " ,  
                                                                             " p u l s e   i n d e x " ,   [ ' 1 ' ,   ' 2 ' ,   ' 3 ' ] ,  
                                                                             e d i t a b l e = F a l s e )  
                 i f   o k :  
                         p = i n t ( i d x ) - 1  
                         l = s e l f . m p l P u l s e s . a x . g e t _ l i n e s ( )  
                         i f   p = = 2 :  
                                 l [ 2 ] . s e t _ y d a t a ( l [ 0 ] . g e t _ y d a t a ( ) - l [ 1 ] . g e t _ y d a t a ( ) )  
                         i f   p = = 0 :  
                                 l [ 0 ] . s e t _ y d a t a ( l [ 1 ] . g e t _ y d a t a ( ) + l [ 1 ] . g e t _ y d a t a ( ) )  
                                 l [ 3 ] . s e t _ y d a t a ( l [ 0 ] . g e t _ y d a t a ( ) - l [ 1 ] . g e t _ y d a t a ( ) )  
                         i f   p = = 1 :  
                                 l [ 1 ] . s e t _ y d a t a ( l [ 0 ] . g e t _ y d a t a ( ) - l [ 2 ] . g e t _ y d a t a ( ) )  
                                 l [ 3 ] . s e t _ y d a t a ( l [ 0 ] . g e t _ y d a t a ( ) - l [ 1 ] . g e t _ y d a t a ( ) )  
                         s e l f . m p l R e d r a w ( )  
                  
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " :  
         a p p   =   Q A p p l i c a t i o n ( s y s . a r g v )  
         w i n d o w   =   M y W i n d o w ( )  
         w i n d o w . s h o w ( )  
         s y s . e x i t ( a p p . e x e c _ ( ) ) 