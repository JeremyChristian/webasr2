<?php $audio = kopa_content_get_audio( get_the_content() ); 
$kopa_setting = kopa_get_template_setting();
$layout_id = $kopa_setting['layout_id'];
?>
<li id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
    <article class="entry-item audio-post <?php echo $layout_id == 'blog-2-right-sidebar' ? 'clearfix' : ''; ?>">
        <?php if ( ! empty( $audio ) ) : ?> 
            <div class="entry-thumb">
                <?php
                    $audio = $audio[0];
                    echo do_shortcode( $audio['shortcode'] ); 
                ?>
            </div>
        <?php endif; ?>
        <div class="entry-content">
            <header>
                <h6 class="entry-title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a><span></span></h6>
                <span class="entry-date"><span class="fa fa-clock-o"></span><?php the_time( get_option( 'date_format' ) ); ?></span>
                <span class="entry-comments"><span class="fa fa-comment"></span><?php comments_popup_link(); ?></span>
            </header>
            <?php the_excerpt(); ?>
            <a class="more-link clearfix" href="<?php the_permalink(); ?>"><?php _e( 'Read more', kopa_get_domain() ); ?> <span class="fa fa-forward"></span></a>
        </div>
    </article><!--entry-item-->
</li>