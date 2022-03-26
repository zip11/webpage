::Èí¼ş ½âÂë£¬amd gpu±àÂë
cd /d %~dp0
set mz="*.mp4"
ffmpeg  -i %mz%  -c:v  h264_amf   -vf scale=1920:1080 -quality balanced -rc cqp -qp_i 25 -qp_p 25 -qp_b 25 -c:a copy  -ss 00:00:10 -to 00:02:15  "a.mkv"

pause