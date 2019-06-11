/*！
 *	Vue-slideshow v1.1.0
 *	
 * 	Copyright (C) 2019, ZhaoGang
 * 	Released under the MIT license
 *
 *  Update: 2019-04-20
 */
!(( document, window, Vue ) => {

	"use strict";

	function $ ( selector, context ) {
		return ( context || document ).querySelector( selector );
	}
	function $$ ( selector, context ) {
		return [].slice.call( ( context || document ).querySelectorAll( selector ) );
	}

	if ( !$( "style.v-slideshow-style" ) ) {
		$( "head" ).insertAdjacentHTML( "beforeend", `<style class="v-slideshow-style">.v-slideshow-container{position:relative;width:100%;height:100%;margin:0;padding:0;overflow:hidden;background:#fff}.v-slideshow-wrapper{position:absolute;height:100%;margin:0;padding:0}.v-slideshow-box,.v-slideshow-box a,.v-slideshow-box img{position:absolute;width:100%;height:100%}.v-slideshow-box a,.v-slideshow-box img{display:block;border:0}.v-slideshow-box-fade{opacity:0;transition:.7s;display:none}.v-slideshow-box-show{opacity:1}.v-slideshow-box-block{display:block}.v-slideshow-box.v-slideshow-block{display:block}.v-slideshow-dot{position:absolute;height:10px;bottom:20px;left:50%;transform:translateX(-50%)}.v-slideshow-dot i{display:block;float:left;cursor:pointer;width:10px;height:10px;border-radius:50%;background:rgba(255,255,255,.5);margin:0 5px;transition:.3s}.v-slideshow-dot i.active{background:rgba(255,255,255,1)}.v-slideshow-arrow i{display:block;width:40px;height:40px;background-image:url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNTU1NzI0MjA4NjA5IiBjbGFzcz0iaWNvbiIgc3R5bGU9IiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjIyOTAiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMjgiIGhlaWdodD0iMjgiPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PC9zdHlsZT48L2RlZnM+PHBhdGggZD0iTTY3MC42NzY5MjkgNzc3LjU5Mjk4NCA0MDMuNjI3NzggNTEzLjM2MjAyMWwyNjUuMzIwNzg1LTI2OC4xNDYxMzNjMTEuNzc2MjA4LTExLjc3NTE4NCAxMS43MzQyNTItMzAuOTA4OTY0LTAuMDkxMDc0LTQyLjczNDI5bC0wLjAwMTAyMyAwYy0xMS44MjUzMjYtMTEuODI2MzUtMzAuOTU4MDgyLTExLjg2NzI4Mi00Mi43MjgxNSAyLjkzMDc0OUwzNDMuMTAwMjQyIDQ4OC40NDA0MjFjLTMuODE3OTU1IDQuMjczMzI3LTguMjA1ODkyIDkuMzIxMjk2LTguOTMzNDYzIDEyLjA0NTMzNy00LjQ3MDgyNSAxMS4xMTIwODItMi4yMzI4NTQgMjQuNzY1MDMzIDYuNzEwODQyIDM1Ljk4NzYzMmwyODYuOTgyMTMgMjg2Ljk4MjEzYzExLjg3NTQ2OCA4Ljg0NzUwNSAzMS4wOTYyMjkgOC44OTM1NTQgNDIuOTIyNTc4LTIuOTMyNzk2QzY4Mi42MDY2MzMgODA4LjY5NjM3NiA2ODIuNTYwNTg0IDc4OS40NzY2MzkgNjcwLjY3NjkyOSA3NzcuNTkyOTg0eiIgcC1pZD0iMjI5MSIgZmlsbD0iI2ZmZmZmZiI+PC9wYXRoPjwvc3ZnPg==");background-color:rgba(0,0,0,.5);background-position:center;background-repeat:no-repeat;position:absolute;top:50%;border-radius:50%;cursor:pointer;transform:translateY(-50%)}.v-slideshow-arrow i:first-child{left:15px}.v-slideshow-arrow i:last-child{right:15px;transform:translateY(-50%) rotate(180deg)}</style>
		` );
	}

	Vue.component("vue-slideshow", {
		template: `
			<div 
				class="v-slideshow-container" 
				:data-custom-arrow="Array.isArray( config.arrow ) && config.arrow.join( '|' )" 
				:data-custom-dot="typeof config.dot === 'string' && config.dot" 
				:data-id="'v-slideshow-id-' + Date.now() + ~~(Math.random() * 100000000)"
				@mouseenter="enter" 
				@mouseleave="leave"
			>
				<div class="v-slideshow-wrapper" :style="wrapperStyle">
					<div class="v-slideshow-box" v-if="config.effect === 'slide'" :style="boxStyle( 0 )">
						<a :href="data[ data.length - 1 ].href"><img :src="data[ data.length - 1 ].src"></a>
					</div>
					<div v-for="( list, index ) in data" :class="boxClass( index )" :style="boxStyle( index + 1 )">
						<a :href="list.href"><img :src="list.src"></a>
					</div>
					<div class="v-slideshow-box" v-if="config.effect === 'slide'" :style="boxStyle( data.length + 1 )">
						<a :href="data[ 0 ].href"><img :src="data[ 0 ].src"></a>
					</div>
				</div>
				<div class="v-slideshow-arrow" v-if="config.arrow !== false && !Array.isArray( config.arrow )">
					<i @click="arrowEvent( 0 )"></i>
					<i @click="arrowEvent( 1 )"></i>
				</div>
				<div class="v-slideshow-dot" v-if="config.dot !== false && typeof config.dot !== 'string'">
					<i v-for="( n, index ) in data" v-if="index < data.length" :class="dotIClass( index )" @click="dotEvent( index )"></i>
				</div>
			</div>
		`,
		props: [ "data", "config" ],
		computed: {
			wrapperStyle: function () {
				return {
					width: this.config.effect === "slide" ? ( `${ 100 * ( this.data.length + 2 ) }%` ) : "100%",
					transform: this.config.effect === "slide" && `translateX(-${ 100 / ( this.data.length + 2 ) }%)`
				}
			},
			boxClass: function () {
				return function ( index ) {
					return {
						"v-slideshow-box": true,
						"v-slideshow-box-fade": this.config.effect === "fade" && true,
						"v-slideshow-box-show": this.config.effect === "fade" && index === 0,
						"v-slideshow-box-block": this.config.effect === "fade" && index === 0
					}
				}
			},
			boxStyle: function () {
				return function ( index ) {
					return {
						width: `${ this.config.effect !== "slide" ? 100 : ( 100 / ( this.data.length + 2 ) ) }%`,
						left: this.config.effect === "slide" && `${ 100 / ( this.data.length + 2 ) * index }%`
					}
				}
			},
			dotIClass: function () {
				return function ( index ) {
					return {
						active: index === 0
					}
				}
			}
		},
		methods: {
			slide: function ( index ) {
				const ID = window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ];

				ID.animated = true;
				const w = 100 / ( this.data.length + 2 );
				const length = this.data.length;

				this.dotChange( index, this.config.dot );
				if ( index === -1 ) {
					this.dotChange( length - 1, this.config.dot );
				}
				if ( index === length ) {
					this.dotChange( 0, this.config.dot );
				}
				
				const $wrapper = this.$el.querySelector( ".v-slideshow-wrapper" );
				$wrapper.style.transition = ".7s";
				requestAnimationFrame(() => {
					$wrapper.style.transform = `translateX(-${ w * ( index + 1 ) }%)`;
				})
				
				const timer = window.setTimeout(() => {
					$wrapper.style.transition = "0s";
					if ( index === length ) {
						ID.imageIndex = 0;
						$wrapper.style.transform = `translateX(-${ w }%)`;
					}
					if ( index === -1 ) {
						ID.imageIndex = length - 1;
						$wrapper.style.transform = `translateX(-${ w * length }%)`;
					}
					window.clearTimeout( timer );
					ID.animated = false;
				}, 700)
			},
			fade: function ( index ) {
				const ID = window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ];

				ID.animated = true;
				this.dotChange( index, this.config.dot );
				const $box = $$( ".v-slideshow-box", this.$el );
				$box.forEach(function ( box, item ) {
					if ( item === index ) {
						box.classList.add( "v-slideshow-box-block" );
						const timer_1 = window.setTimeout(function () {
							box.classList.add( "v-slideshow-box-show" );
							window.clearTimeout( timer_1 );
						}, 16);
					} else {
						box.classList.remove( "v-slideshow-box-show" );
						const timer_2 = window.setTimeout(function () {
							box.classList.remove( "v-slideshow-box-block" );
							window.clearTimeout( timer_2 );
							ID.animated = false;
						}, 700);
					}
				})
			},
			dotChange: function ( index, useCustomDot ) {
				window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ].imageIndex = index;
				const $dot = typeof useCustomDot === "string" ? [].slice.call( $( useCustomDot ).children ) : $$( ".v-slideshow-dot i", this.$el );  
				$dot.forEach(function ( dot, item ) {
					dot.classList.remove( "active" );
					if ( item === index ) {
						dot.classList.add( "active" );
					}
				})
			},
			dotEvent: function ( index, useCustomDot ) {
				if ( !window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ].animated ) {
					this[ this.config.effect === "fade" ? "fade" : "slide" ]( index );
					this.dotChange( index, useCustomDot );
				}
			},
			arrowEvent: function ( i ) {
				if ( !window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ].animated ) {
					const ID = window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ];
					if ( i ) {
						ID.imageIndex++;
						if ( ID.imageIndex > this.data.length - 1 && this.config.effect !== "slide" ) {
							ID.imageIndex = 0;
						}
					} else {
						ID.imageIndex--;
						if ( ID.imageIndex < 0 && this.config.effect !== "slide" ) {
							ID.imageIndex = this.data.length - 1;
						}
					}
					if ( this.config.effect === "fade" ) {
						this.fade( ID.imageIndex );
					} else {
						this.slide( ID.imageIndex );
					}
				}
			},
			enter: function () {
				this.config.autoplay && window.clearInterval( window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ].autoTimer );
			},
			leave: function () {
				this.config.autoplay && this.play();
			},
			play: function () {
				window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ].autoTimer = window.setInterval(() => {
					this.arrowEvent( 1 );
				}, ~~this.config.autoplay);
			}
		},
		mounted: function () {

			if ( !window.VueSlideShowIDCache ) {
				window.VueSlideShowIDCache = {};
			}
			window.VueSlideShowIDCache[ this.$el.getAttribute( "data-id" ) ] = {
				imageIndex: 0,
				animated: false,
				autoTimer: null
			};

			this.config.autoplay && this.play();

			let customArrow = this.$el.getAttribute( "data-custom-arrow" );
			if ( customArrow ) {
				customArrow = customArrow.split( "|" );
				$( customArrow[ 0 ] ).onclick = () => this.arrowEvent( 0 );
				$( customArrow[ 1 ] ).onclick = () => this.arrowEvent( 1 );
			}

			let customDot = this.$el.getAttribute( "data-custom-dot" );
			if ( customDot ) {
				[].slice.call( $( customDot ).children ).forEach(( dot, item ) => {
					if ( item > this.data.length - 1 ) {
						return;
					}
					dot.onclick = () => this.dotEvent( item, this.config.dot );
				})
			}
		}
	});

	Vue.prototype.VueSlideShow = function ( selector, options ) {
		$( selector ).innerHTML = `<vue-slideshow :data="images" :config="config"></vue-slideshow>`;
		return new Vue({
			el: selector,
			data: {
				images: options.images,
				config: options.config
			}
		});
	}

})( document, window, Vue );