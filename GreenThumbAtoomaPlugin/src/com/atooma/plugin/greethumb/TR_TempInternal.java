package com.atooma.plugin.greethumb;

import org.json.JSONException;
import org.json.JSONObject;

import android.content.Context;
import android.os.RemoteException;
import android.util.Log;

import com.atooma.plugin.AlarmBasedTrigger;
import com.atooma.plugin.ParameterBundle;
import com.atooma.plugin.Schedule;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;

public class TR_TempInternal extends AlarmBasedTrigger {

	private static final long INTERVAL = 30 * 1000;

	public TR_TempInternal(Context context, String id, int version) {
		super(context, id, version);
	}

	@Override
	public void declareParameters() {
		addParameter(R.string.address, R.string.address, "ADDRESS", "STRING", true, null);
		addParameter(R.string.pin, R.string.pin, "PIN", "NUMBER", true, null);
		addParameter(R.string.filter_temp, R.string.filter_temp, "FILTER", "NUMBER", true, null);
	}

	@Override
	public Schedule getScheduleInfo() throws RemoteException {
		return new Schedule.Builder()
				.exact(false)
				.interval(INTERVAL)
				.repeat(true)
				.triggerAtTime(System.currentTimeMillis())
				.wakeup(false).build();
	}

	@Override
	public void defineUI() {
		setIcon(R.drawable.icon_temp_inside);
		setTitle(R.string.tr_tempint);
	}

	@Override
	public void onRevoke(String arg0) {

	}

	@Override
	public void onTimeout(final String ruleId, ParameterBundle parameters) {
		String baseUrl = (String) parameters.get("ADDRESS");
		int pin = Utils.doubleToInt((Double) parameters.get("PIN"));
		final Double filter = (Double) parameters.get("FILTER");

		String url = baseUrl + "/api/sensors/dht/" + pin + "/";
		
		Log.e("CALLEDURL", "URL" + url);

		AsyncHttpClient client = new AsyncHttpClient();
		client.get(url, new AsyncHttpResponseHandler() {

			@Override
			public void onSuccess(String response) {
				try {
					JSONObject json = new JSONObject(response);
					int level = json.getInt("temperature");
					if (level < filter)
						trigger(ruleId, new ParameterBundle());
				} catch (JSONException e) {
					e.printStackTrace();
				}
			}

		});
	}

}
