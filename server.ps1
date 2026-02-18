$l = [System.Net.HttpListener]::new()
$l.Prefixes.Add("http://localhost:8082/")
try {
    $l.Start()
    Write-Host "Server started on http://localhost:8082/"
    while ($l.IsListening) {
        $c = $l.GetContext()
        $urlPath = $c.Request.Url.LocalPath
        if ($urlPath -eq "/") { $urlPath = "/index.html" }
        $p = Join-Path (Get-Location) ($urlPath.TrimStart('/'))
        
        if (Test-Path $p -PathType Leaf) {
            $ext = [System.IO.Path]::GetExtension($p).ToLower()
            $contentType = switch ($ext) {
                ".html" { "text/html" }
                ".css" { "text/css" }
                ".js" { "application/javascript" }
                ".jpg" { "image/jpeg" }
                ".jpeg" { "image/jpeg" }
                ".png" { "image/png" }
                ".svg" { "image/svg+xml" }
                default { "application/octet-stream" }
            }
            $c.Response.ContentType = $contentType
            $b = [System.IO.File]::ReadAllBytes($p)
            $c.Response.ContentLength64 = $b.Length
            $c.Response.OutputStream.Write($b, 0, $b.Length)
        }
        else {
            $c.Response.StatusCode = 404
        }
        $c.Response.Close()
    }
}
catch {
    Write-Error $_
}
finally {
    $l.Stop()
}
