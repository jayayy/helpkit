sobjectName="Voice_Call_Metrics__c"
externalId="Vendor_Call_Key__c"
filenameToSplit="ivrJourneys.csv"
linesPerChunk="1400"

head -n 1 $filenameToSplit > header.csv
tail -n +2 $filenameToSplit | split -l $linesPerChunk -d - chunk_

for file in chunk_*; do
    mv "$file" "$file.csv"
done

for file in chunk_*.csv; do``
    cat header.csv "$file" > temp && mv temp "$file"
done

for file in chunk_*.csv; do
    filename=$(basename "$file")
    sf data upsert bulk --sobject $sobjectName --file $filename --external-id $externalId
done

rm chunk_*.csv
