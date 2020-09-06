import React from 'react';
import '../../App.css';
import Footer from '../Footer';

export default function face_rec() {

  return (
    <>
    <h1 className='face_rec'>FACIAL RECOGNITION</h1>;

    <form method = 'post' enctype='multipart/form-data'>
      <p>
        <input type='file' name='file'/>
        <input type='submit' value='Upload'/>
      </p>
    </form>


      <Footer />
    </>
  );
}
