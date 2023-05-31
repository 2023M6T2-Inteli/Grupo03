import { useState } from 'react';
import { createClient } from '@supabase/supabase-js';
import { useMediaRecorder } from 'react-media-recorder';

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_KEY;

const supabase = createClient(supabaseUrl, supabaseKey);

const WebcamRecorder = () => {
  const { status, startRecording, stopRecording, mediaBlobUrl } = useMediaRecorder({
    video: true,
    onStop: async (blobUrl) => {
      // Envie o vídeo para o Supabase
      const bucketName = 'nome-do-seu-bucket(video)';
      const fileName = 'video.webm'; // ou qualquer nome de arquivo adequado
      
      const { data, error } = await supabase.storage
        .from(bucketName)
        .upload(blobUrl, fileName);

      if (error) {
        console.error('Erro ao enviar o vídeo para o Supabase:', error);
      } else {
        console.log('Vídeo enviado com sucesso!');
      }
    },
  });

  return (
    <div>
      <video src={mediaBlobUrl} autoPlay muted />
      {status === 'idle' && <button onClick={startRecording}>Iniciar Gravação</button>}
      {status === 'recording' && <button onClick={stopRecording}>Parar Gravação</button>}
    </div>
  );
};

export default WebcamRecorder;