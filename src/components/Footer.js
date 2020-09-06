import React from 'react';
import './Footer.css';
import { Button } from './Button';
import { Link } from 'react-router-dom';

function Footer() {
  return (
    <div className='footer-container'>
      <section className='footer-subscription'>
        <p className='footer-subscription-heading'>
          To learn more about the creators feel free to check out these links below:
        </p>
        {
          /*
          <div className='input-areas'>
          <form>
            <input
              className='footer-input'
              name='email'
              type='email'
              placeholder='Your Email'
            />
            <Button buttonStyle='btn--outline'>Subscribe</Button>
          </form>
        </div>
          */
        }

      </section>
      <div class='footer-links'>
        <div className='footer-link-wrapper'>
          <div class='footer-link-items'>
            {/*add teams linked in links here*/}
            <h2>About Us</h2>
            <a href='https://www.linkedin.com/in/daniel-chamorro-847618199/' target='_blank'
              rel='noopener'>
                Daniel Chamorro
            </a>

            <a href='https://www.linkedin.com/in/bryce-bodner-2767171b5/' target='_blank'
              rel='noopener'>
                Bryce Bodner
            </a>

            <a href='https://www.linkedin.com/in/alexander-ling-6b8a28178/' target='_blank'
              rel='noopener'>
                Alex Ling
            </a>

            <a href='https://www.linkedin.com/in/apsaramitra' target='_blank'
              rel='noopener'>
                Apsara Mitra
            </a>

          </div>
          <div class='footer-link-items'>
            <h2>Contact Us</h2>
            <Link to='/'>Contact</Link>
            <Link to='/'>Support</Link>
          </div>
        </div>
        <div className='footer-link-wrapper'>
        </div>
      </div>
      <section class='social-media'>
        <div class='social-media-wrap'>
          <div class='footer-logo'>
            <Link to='/' className='social-logo'>
              Spy Tools
              <i class='fab fa-typo3' />
            </Link>
          </div>
          <small class='website-rights'>Spy Tools © 2020</small>
          <div class='social-icons'>

            <a
              class='social-icon-link github'
              href='https://github.com/alexling540/howdyhack2020'
              target='_blank'
              rel='noopener'
              aria-label='Github'
            >
              <i class='fab fa-github' />
            </a>
            
            <a
              class='social-icon-link twitter'
              href='https://www.linkedin.com/in/daniel-chamorro-847618199/'
              target='_blank'
              rel='noopener'
              aria-label='LinkedIn'
            >
              <i class='fab fa-linkedin' />
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Footer;
