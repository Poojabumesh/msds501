directory="$1"

mkdir -p $directory/images
mkdir -p $directory/videos
mkdir -p $directory/documents

for file in "$directory"/*; do
filename=$(basename "$file")
	if [[ "${file##*.}" = "jpg" ]]; then
	echo "at jpg"
	mv "$file" "images/new_$filename"
	fi

	if [[ "${file##*.}" = "mp4" ]]; then
	mv "$file" "videos/new_$filename"
	echo "at mp4"
	fi

	if [[ "${file##*.}" = "txt" ]]; then
	mv "$file" "documents/new_$filename"
	echo "at txt"
	fi
done


